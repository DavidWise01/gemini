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

## STOICHEION elemental corpus expansion · 2026-11-23

[Open the STOICHEION / Elemental Corpus gallery](./stoicheion.html). [Source inventory JSON](./evidence/stoicheion-elemental-corpus-2026-11-23.json) anchors the project to the user-published STOICHEION 256-axiom register and the separate 118 Gates / Stochien Element mapping. The inventory contains a scoped set of verified READMEs, excerpts, dated commits, and discovered repositories. It is **not a complete crawl of every repository or Git history**. The STOICHEION README's claimed 2026-02-02 prior-art date and copyright IDs are attributed to the repository, not independently authenticated.

## Primary source baseline — STOICHEION uploaded manuals

The author-supplied **STOICHEION Complete Technical Manual**, labeled v1.0 April 2026, is the documentary baseline. Read the [book-first online reader](./manual.html), the [final manuscript source](./source/STOICHEION_COMPLETE_MANUAL_FINAL.md), and the [expanded alternative](./source/STOICHEION_Complete_Manual_variant.md). [Full original attachment manifest with SHA256](./evidence/stoicheion-upload-manifest-2026-11-23.json) lists the EPUB, three cover uploads, multipart drafts and their exact local-file digests. GitHub contains the text editions and a CSS interpretation of the supplied cover; **original JPEG and EPUB bytes are not committed**. Two cover uploads are byte-identical. All document-level prior-art, testing, and publication assertions remain attributed to the source rather than independently verified.
