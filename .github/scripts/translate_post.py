#!/usr/bin/env python3
"""
Translates a Hungarian Jekyll blog post to English using the Claude API.

Usage:
    python translate_post.py <input_hu.md>
    python translate_post.py <input_hu.md> <output_en.md>

If output path is not given, it is derived by appending -en before .md.

Requirements:
    pip install anthropic pyyaml

Environment:
    ANTHROPIC_API_KEY  — Anthropic API key (required at runtime)
"""

import sys
import os
import re
import time
import yaml
from anthropic import Anthropic, AuthenticationError


# ---------------------------------------------------------------------------
# Front matter parsing
# ---------------------------------------------------------------------------

def split_front_matter(content: str) -> tuple:
    """
    Split Jekyll markdown into (front_matter_dict, body_str).
    Returns ({}, content) if no valid front matter is found.
    """
    if not content.startswith("---"):
        return {}, content

    end = content.find("\n---", 3)
    if end == -1:
        return {}, content

    yaml_str = content[3:end].strip()
    body = content[end + 4:].lstrip("\n")

    try:
        fm = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError as exc:
        print(f"[ERROR] YAML parse failed: {exc}")
        return {}, content

    return fm, body


def reconstruct(fm: dict, body: str) -> str:
    """Reconstruct Jekyll markdown from a front matter dict and body string."""
    # Use a custom representer so None stays as an empty value (not 'null')
    class SafeDumperNoNull(yaml.SafeDumper):
        pass

    def represent_none(dumper, _):
        return dumper.represent_scalar("tag:yaml.org,2002:null", "")

    SafeDumperNoNull.add_representer(type(None), represent_none)

    yaml_str = yaml.dump(
        fm,
        Dumper=SafeDumperNoNull,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    return f"---\n{yaml_str}---\n\n{body}"


# ---------------------------------------------------------------------------
# Output validation
# ---------------------------------------------------------------------------

def validate_output(content: str) -> bool:
    """Return True if the generated content looks like a valid Jekyll post."""
    if not content or len(content.strip()) < 50:
        print("[VALIDATE] Content is empty or too short")
        return False

    fm, body = split_front_matter(content)
    if not fm:
        print("[VALIDATE] No valid front matter")
        return False
    if "title" not in fm or "date" not in fm:
        print("[VALIDATE] Missing required front matter fields (title, date)")
        return False
    if not body or len(body.strip()) < 20:
        print("[VALIDATE] Body is empty or too short")
        return False

    return True


# ---------------------------------------------------------------------------
# Claude API interaction
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = (
    "You are a professional translator specializing in bonsai, horticulture, "
    "and Japanese maple content. You translate Hungarian text to natural, "
    "expert-level English while strictly preserving all technical markup."
)

# Fields whose string values should be translated
SIMPLE_FIELDS = ("title", "subtitle")
# List fields that may be translated
LIST_FIELDS = ("categories", "tags")

# Bonsai terms that must NOT be translated
PRESERVE_TERMS = "nebari, ramification, wabi-sabi, jin, shari, apex"


def build_prompt(fm: dict, body: str) -> str:
    """Build the translation prompt, sending only translatable content."""

    # Collect only the fields we want translated
    fields_to_translate: dict = {}
    for key in SIMPLE_FIELDS:
        if key in fm and fm[key]:
            fields_to_translate[key] = fm[key]
    for key in LIST_FIELDS:
        if key in fm and fm[key]:
            fields_to_translate[key] = fm[key]

    fields_yaml = yaml.dump(
        fields_to_translate,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )

    return f"""Translate the components below from Hungarian to English.

=== STRICT RULES ===
- Translate ONLY what is explicitly provided here.
- Keep Japanese/bonsai technical terms as-is: {PRESERVE_TERMS}
- Use "Japanese maple" for "japán juhar".
- Keep cultivar names unchanged (e.g. Beni chidori, Arakawa, Katsura).
- In the BODY: preserve ALL markdown formatting (##, **, _, lists, blockquotes) exactly.
- In the BODY: preserve ALL HTML tags and their attributes EXACTLY (including src, style, class, etc.).
- In the BODY: preserve ALL image paths (/assets/...) EXACTLY unchanged.
- In the BODY: preserve ALL Liquid/Jekyll includes EXACTLY unchanged.
- In the BODY: preserve ALL URLs exactly unchanged.
- Translate alt= text inside HTML tags if it is in Hungarian.
- Maintain the warm, expert, personal tone of the original.
- Do NOT add commentary, preamble, or post-script.

=== FRONT MATTER VALUES TO TRANSLATE ===
{fields_yaml}
=== ARTICLE BODY TO TRANSLATE ===
{body}
=== END ===

Respond in this EXACT format with no text before or after:

FRONT_MATTER:
<translated front matter values as YAML, using the exact same keys>
BODY:
<translated article body>
"""


def parse_response(response_text: str, original_fm: dict) -> tuple:
    """
    Parse the structured response. Returns (new_fm_dict, body_str).
    Raises ValueError if the response cannot be parsed.
    """
    fm_marker = "FRONT_MATTER:"
    body_marker = "BODY:"

    if fm_marker not in response_text or body_marker not in response_text:
        raise ValueError("Response missing FRONT_MATTER: or BODY: markers")

    fm_start = response_text.index(fm_marker) + len(fm_marker)
    body_start = response_text.index(body_marker)

    if fm_start >= body_start:
        raise ValueError("FRONT_MATTER: section must come before BODY:")

    fm_yaml_str = response_text[fm_start:body_start].strip()
    body = response_text[body_start + len(body_marker):].strip()

    try:
        translated_values = yaml.safe_load(fm_yaml_str) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"Could not parse translated front matter YAML: {exc}") from exc

    # Build new front matter: start from original, overlay translated values, add lang
    new_fm = dict(original_fm)
    for key in SIMPLE_FIELDS + LIST_FIELDS:
        if key in translated_values and translated_values[key]:
            new_fm[key] = translated_values[key]
    new_fm["lang"] = "en"

    return new_fm, body


# ---------------------------------------------------------------------------
# Main translation function
# ---------------------------------------------------------------------------

def translate_post(input_path: str, output_path: str = None, max_retries: int = 3) -> str:
    """
    Translate a Hungarian Jekyll post to English.

    Returns output_path on success, None on failure.
    Never overwrites an existing file.
    """
    if output_path is None:
        if input_path.endswith(".md"):
            output_path = input_path[:-3] + "-en.md"
        else:
            output_path = input_path + "-en.md"

    # Safety: never overwrite
    if os.path.exists(output_path):
        print(f"[SKIP] Already exists: {output_path}")
        return output_path

    # Read input
    try:
        with open(input_path, "r", encoding="utf-8") as fh:
            content = fh.read()
    except OSError as exc:
        print(f"[ERROR] Cannot read {input_path}: {exc}")
        return None

    fm, body = split_front_matter(content)
    if not fm:
        print(f"[ERROR] No front matter in {input_path}, skipping")
        return None

    # Honour the english: no switch
    if str(fm.get("english", "")).strip().lower() == "no":
        print(f"[SKIP] english: no — {input_path}")
        return output_path  # treat as "done" so batch doesn't fail

    # Check API key before doing anything else
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        print("[WARNING] ANTHROPIC_API_KEY is not set — skipping translation")
        sys.exit(0)

    client = Anthropic()
    prompt = build_prompt(fm, body)

    last_error = None
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[API] {input_path} (attempt {attempt}/{max_retries})")
            message = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=8192,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            response_text = message.content[0].text

            new_fm, new_body = parse_response(response_text, fm)
            result = reconstruct(new_fm, new_body)

            if not validate_output(result):
                raise ValueError("Output failed validation")

            with open(output_path, "w", encoding="utf-8") as fh:
                fh.write(result)

            print(f"[OK] {input_path} → {output_path}")
            return output_path

        except AuthenticationError as exc:
            # Wrong API key — retrying will never help
            print(f"[ERROR] Authentication failed: invalid API key")
            print("        Set ANTHROPIC_API_KEY to a valid key and try again.")
            sys.exit(1)

        except Exception as exc:
            last_error = exc
            print(f"[ATTEMPT {attempt}/{max_retries}] Failed: {exc}")
            if attempt < max_retries:
                wait = 2 ** attempt
                print(f"[RETRY] Waiting {wait}s...")
                time.sleep(wait)

    print(f"[FAIL] Giving up on {input_path}: {last_error}")
    return None


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = translate_post(in_file, out_file)
    sys.exit(0 if result else 1)
