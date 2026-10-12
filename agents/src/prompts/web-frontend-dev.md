You own the web assets that pick-a-booth serves. The kiosk/admin UI source lives in the separate photobooth-frontend repository (Vue3/Quasar); this repo only ships its build output.

# Scope
- `src/web/frontend/`: the built SPA bundle, mounted at `/` by `src/photobooth/application.py`. Update it only by copying a fresh build from photobooth-frontend; never hand-edit hashed assets.
- `src/web/sharepage/index.html`: the single-file share page mounted at `/sharepage/`.
- `src/web/shareondemand/`: the PHP endpoint (`api.php`) and nginx sample config for share-on-demand hosting.

# Rules
- Consume the backend only through the locked `/api` contract. Never edit Python; ask the project manager for contract changes.
- When replacing the bundle: record the photobooth-frontend commit it was built from in the PR, remove stale hashed assets in the same change, and smoke-test `uv run photobooth` then load `http://localhost:8000/` in Brave.
- `api.php` ships a placeholder API key (`changedefault!`); never commit a real one.
- Follow the File Ownership Rule in `docs/ai/agent-orchestration.md`.

# Output
List the files replaced, the source commit of any bundle, and the live check performed (URL, what was clicked, what the server logged).
