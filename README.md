# Gemini · HAKA / WAKA / HANA / KU

Four-chamber, single-screen interactive evidence atlas exploring the dated public Git history of chemical names and the reported Gemini Helium naming scheme.

**Pages target:** https://davidwise01.github.io/gemini/ (requires GitHub Pages enabled with **GitHub Actions** as source; workflow included).

## Four chambers

- **HAKA**: source root — earliest visible matching commit
- **WAKA**: sequence — chronological ordering
- **HANA**: chemistry — element-name lattice
- **KU**: boundary — unknown ancestry, no assumed causal link

These chamber descriptions are **UI labels**, not assertions of traditional linguistic definitions.

## Provenance

[Chronology JSON](./evidence/chemistry-chronology-2026-11-23.json) preserves six source commits from May 27 through November 2, 2026. [External Helium candidate](https://github.com/DavidWise01/convergence/blob/main/evidence/candidates/2026-11-23-gemini-4-helium-naming.json) is held separately. **Prior dated commits do not prove a transmission or copying relationship.** Commit-message search is not an exhaustive first-use audit.

## Build & publishing

Open `index.html` locally in any modern browser, or use `python3 -m http.server 8000`. No runtime dependencies, tracking, external scripts, or privileged APIs. Motion can be paused; reduced-motion settings are respected. The repository includes `.github/workflows/pages.yml` for Pages deployment. Check [Actions](https://github.com/DavidWise01/gemini/actions) before claiming a live deployment.

`{{ source → dated evidence → hypothesis boundary }} · .dlw`
