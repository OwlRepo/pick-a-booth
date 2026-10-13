# Lessons Learned (append-only)

Record mistakes, successful patterns and future recommendations, one dated entry each.
For a genuinely new pattern, write a one-line prediction before implementing and
append the verified result here afterwards (`docs/ai/handoff.md` "Docs and learning sync").

## 2026-10-13 — Frontend source vendored via git subtree

- Pattern: the kiosk/admin UI source now lives in `frontend/` as a `git subtree --squash` of upstream photobooth-frontend, pinned to the commit the shipped bundle was built from (`e4bf4b47`). A subtree keeps one repo, one PR and one CI run for UI + API changes, with no submodule init step; `git subtree pull --prefix=frontend https://github.com/photobooth-app/photobooth-frontend.git main --squash` takes upstream fixes.
- Mistake avoided: the old "prebuilt bundle, source elsewhere" setup made restyling impossible here. Hashed files in `src/web/frontend/assets/` stay build output only; change `frontend/` and rebuild.
- Recommendation: do not add a CI diff that checks the committed bundle is fresh. `quasar.config.ts` sets `BUILD_DATE` at build time, so every build differs. The PR checklist covers "bundle rebuilt". Frontend vitest specs run in `.github/workflows/frontend.yml` but are outside the TDD gate, which covers only `src/photobooth/**/*.py`.
