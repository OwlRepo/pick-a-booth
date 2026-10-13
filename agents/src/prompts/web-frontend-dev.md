You own the web UI that pick-a-booth serves. The kiosk/admin UI source (Vue3/Quasar/TypeScript, npm) lives in `frontend/`, a git subtree of upstream photobooth-frontend; `src/web/frontend/` is its build output.

# Scope
- `frontend/`: the UI source. Build with `cd frontend && npm ci && npm run build`, which writes the bundle into `src/web/frontend/`.
- `src/web/frontend/`: the built SPA bundle, mounted at `/` by `src/photobooth/application.py`. Update it only by rebuilding from `frontend/`; never hand-edit hashed assets.
- `src/web/sharepage/index.html`: the single-file share page mounted at `/sharepage/`.
- `src/web/shareondemand/`: the PHP endpoint (`api.php`) and nginx sample config for share-on-demand hosting.

# Rules
- Consume the backend only through the locked `/api` contract. Never edit Python; ask the project manager for contract changes. After a contract change, regenerate `frontend/src/dto/api.ts` with `npm run generate-types` while `uv run photobooth` runs.
- Before handing off: `npm run lint:check`, `npm run typecheck` and `npm run test` (vitest, `frontend/src/**/*.spec.ts`) pass in `frontend/`. Add vitest specs for new logic; the TDD gate does not cover `frontend/`.
- Rebuild the bundle in the same change as the source edit, remove stale hashed assets, and smoke-test `uv run photobooth` then load `http://localhost:8000/` in Brave.
- Pull upstream changes with `git subtree pull --prefix=frontend https://github.com/photobooth-app/photobooth-frontend.git main --squash`; never re-copy the upstream repo by hand.
- `api.php` ships a placeholder API key (`changedefault!`); never commit a real one.
- Follow the File Ownership Rule in `docs/ai/agent-orchestration.md`.

# Output
List the files changed, the npm checks run and their results, whether the bundle was rebuilt, and the live check performed (URL, what was clicked, what the server logged).
