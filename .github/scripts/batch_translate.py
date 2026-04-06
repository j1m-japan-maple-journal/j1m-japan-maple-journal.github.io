#!/usr/bin/env python3
"""
Batch-translate all Hungarian Jekyll posts that do not yet have an English version.

Scans _posts/*.md, skips files ending in -en.md, and skips any file whose
-en.md counterpart already exists.  Intended to be run once locally to
bootstrap the English post archive, and subsequently as a pre-build step in
GitHub Actions to handle newly added posts.

Usage (from repository root):
    ANTHROPIC_API_KEY=sk-... python .github/scripts/batch_translate.py

Requirements:
    pip install anthropic pyyaml
"""

import os
import sys
import glob

# Allow importing translate_post from the same directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from translate_post import translate_post, split_front_matter  # noqa: E402


def main() -> None:
    posts_dir = "_posts"

    if not os.path.isdir(posts_dir):
        print(f"[ERROR] Directory '{posts_dir}' not found. Run from repository root.")
        sys.exit(1)

    all_posts = sorted(glob.glob(os.path.join(posts_dir, "*.md")))

    # Hungarian source posts only (not already translated)
    hu_posts = [p for p in all_posts if not p.endswith("-en.md")]

    # Filter to those that are missing an EN counterpart and not opted out
    to_translate = []
    for p in hu_posts:
        en_path = p[:-3] + "-en.md"
        if os.path.exists(en_path):
            continue
        try:
            with open(p, "r", encoding="utf-8") as fh:
                fm, _ = split_front_matter(fh.read())
            if str(fm.get("english", "")).strip().lower() == "no":
                print(f"[SKIP] english: no — {p}")
                continue
        except OSError:
            pass
        to_translate.append(p)

    if not to_translate:
        print("Nothing to do — all posts already have English versions.")
        return

    print(f"Found {len(to_translate)} post(s) to translate:\n")
    for p in to_translate:
        print(f"  {p}")
    print()

    succeeded = []
    failed = []

    try:
        for p in to_translate:
            result = translate_post(p)
            if result:
                succeeded.append(p)
            else:
                failed.append(p)
    except KeyboardInterrupt:
        print(f"\n\n[INTERRUPTED] Stopped by user after {len(succeeded)} translation(s).")
        if succeeded:
            print("Completed so far:")
            for s in succeeded:
                print(f"  {s}")
        sys.exit(0)

    print(f"\n{'='*60}")
    print(f"Done: {len(succeeded)}/{len(to_translate)} translated successfully")
    if failed:
        print(f"\nFailed ({len(failed)}):")
        for f in failed:
            print(f"  {f}")
        print(
            "\nHint: Failed posts can be retried by deleting any partial output "
            "(-en.md file) and running this script again."
        )


if __name__ == "__main__":
    main()
