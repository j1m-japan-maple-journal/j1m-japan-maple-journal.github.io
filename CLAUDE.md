# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jekyll static site (jekyll-theme-chirpy 7.4+) deployed to GitHub Pages at a custom domain. Content is a bilingual (Hungarian primary, English auto-translated) blog and knowledge base about Japanese maple bonsai care.

## Commands

```bash
# Development server (live reload, localhost:4000)
bash tools/run.sh

# Production mode
bash tools/run.sh -p

# Build and validate HTML links
bash tools/test.sh

# Install dependencies
bundle install

# Manually run translation (requires ANTHROPIC_API_KEY)
ANTHROPIC_API_KEY=sk-... python .github/scripts/batch_translate.py
```

## Architecture

### Collections

Three Jekyll collections beyond standard posts:

- `_posts/` — Blog posts. Hungarian source files follow `YYYY-MM-DD-slug.md`; English translations are `YYYY-MM-DD-slug-en.md`.
- `_tudas/` — Knowledge base ("Tudástár"). Served at `/tudastar/:name/`. Includes a `Cultivars/` subdirectory.
- `_trees/` — Individual tree tracking. Served at `/trees/:name/`.
- `_tabs/` — Top navigation pages, ordered via front matter `order:` field.

### Bilingual Translation System

Posts are authored in Hungarian and auto-translated to English by a GitHub Actions step that calls the Claude API. The pipeline runs `.github/scripts/batch_translate.py` before the Jekyll build.

- To opt a Hungarian post out of translation, add `english: no` to its front matter.
- The translation script skips posts that already have an `-en.md` counterpart.
- Translation dependencies live in a `.venv/` Python virtual environment: `anthropic pyyaml`.

### Layouts and Includes

Custom layouts override Chirpy defaults:

- `_layouts/post.html` — Extended post template with hero image, YouTube embed, and language switcher (HU/EN toggle).
- `_includes/custom-styles.html` — Global CSS injected into every page.
- `_includes/home-hero.html` — Homepage hero section.

### Last-Modified Dates

`_plugins/posts-lastmod-hook.rb` runs a `git log` for each post during the build and writes the result into `last_modified_at` front matter. This means the build must run inside a git repo with full history.

### Front Matter Conventions

```yaml
layout: post
title: "..."
subtitle: "..."          # optional
date: YYYY-MM-DD
categories: [Category]
tags: [tag1, tag2]
hero_image: /assets/blog/filename.jpg   # optional
youtube_id: abc123       # optional
english: no              # optional — suppresses auto-translation
```

### CI/CD

`.github/workflows/pages-deploy.yml` triggers on push to `main`:
1. Python 3.11 → installs `anthropic pyyaml` → runs batch translation
2. Ruby 3.3 + Bundler → `bundle exec jekyll b` (production mode)
3. Deploys artifact to GitHub Pages
