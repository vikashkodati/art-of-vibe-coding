# Repository Guidelines

## Project Structure & Module Organization
- App source lives in `src/`, with entry points `index.js` and `App.js`, shared styles in `*.css`, and tests alongside components (e.g., `App.test.js`).
- Static assets and HTML shell reside in `public/`; only update files actually needed at runtime.
- Top-level docs (`README.md`, `CLAUDE.md`, `GEMINI.md`) describe workshop flows; keep new guidance scoped to the recipe-sharing frontend.

## Build, Test, and Development Commands
- `npm install` installs dependencies; re-run after updating `package.json` or when switching branches.
- `npm start` launches the React dev server with hot reload at http://localhost:3000.
- `npm run build` produces an optimized production bundle in `build/`; use before deploying demos.
- `npm test` runs Jest in watch mode via `react-scripts`; press `a` for all tests or `q` to quit.

## Coding Style & Naming Conventions
- Use 2 spaces for indentation; avoid tabs to match existing files.
- Stick to functional React components and hooks; keep JSX small and extract helpers into `/src` modules.
- File names should be lowercase with dashes (`recipe-card.js`); co-locate component styles as `component-name.css`.
- ESLint is configured through `react-app`; run `npx eslint src` if you need an explicit check.

## Testing Guidelines
- Jest with React Testing Library is prewired (`setupTests.js`); prefer user-facing assertions from `@testing-library/jest-dom`.
- Name specs `*.test.js` and colocate with the code under test.
- Aim to cover key user flows (render, interactions, API boundaries) and keep tests resilient to UI refactors.

## Commit & Pull Request Guidelines
- Write imperative, concise commit subjects under 72 chars (e.g., `Add recipe list card`).
- Reference related issues in the body and note any follow-up todos.
- Pull requests should summarize scope, list verification commands, and include screenshots for UI changes.

## Security & Configuration Tips
- Never commit secrets; store local values in `.env` and mirror placeholders in `.env.example`.
- Limit Docker or local ports to those already documented; update `docker-compose.yml` if tooling changes.
- Review generated assets before committing to avoid leaking workshop credentials or personal data.
