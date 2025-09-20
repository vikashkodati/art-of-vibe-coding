# Repository Guidelines

This repository hosts workshop materials and agent configs for AI‑assisted development. Keep contributions scoped, practical, and easy to follow.

## Project Structure & Module Organization
- Root docs: `README.md`, `INSTALLATION.md`, `vibe_coding_prompting_patterns.md`
- Steps: `step1/`, `step2/part1`, `step2/part2`, `step3/` (agent configs + guides)
- Dev env: `dockerfile`, `docker-compose.yml`, `docker-compose.*.yml`, `.env.example`
- GitHub config: `.github/`
- Local agent tooling: `.claude/` (do not commit API keys)

## Build, Test, and Development Commands
- Start dev container: `docker compose up -d devbox`
- Attach shell: `docker compose exec devbox bash`
- Stop/cleanup: `docker compose down`
- Validate compose: `docker compose config`
- Quick search (fast): `rg "keyword"` from repo root

## Coding Style & Naming Conventions
- Markdown: Title Case for headings, bullets concise, wrap ≈100 chars.
- Indentation: 2 spaces; no tabs.
- Filenames: lowercase with dashes, e.g., `react-review.toml`, `archibot-agent.md`.
- Paths: follow existing layout (`stepN/partM/...`).
- TOML/YAML: lowercase keys; prefer simple alphanumerics and underscores.
- Keep examples runnable; prefer shell blocks with copy‑paste commands.

## Testing Guidelines
- This repo is documentation‑first; no unit test suite.
- Validate changes by:
  - Checking links and file paths you reference exist.
  - Running `docker compose config` after editing compose files.
  - For `step3/*.toml`, include a minimal example session or usage notes.

## Commit & Pull Request Guidelines
- Commits: Imperative mood, concise subject (<72 chars), detail in body.
- Examples: `Add Docker dev environment`, `Fix Gemini CLI custom commands`.
- PRs must include:
  - Clear description and scope; link related issues.
  - Notable commands to reproduce/verify.
  - Screenshots or snippets when changing docs with output.
  - Updates to `.env.example` when introducing new env vars.

## Security & Configuration Tips
- Never commit secrets. Use `.env` locally; update `.env.example` with placeholders and comments.
- Local tool settings (e.g., `.claude/settings.local.json`) should avoid hard‑coding keys.
- Keep Docker ports minimal and documented in `docker-compose.yml` comments.

