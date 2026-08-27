# DyberPet Fork Roadmap (M1 -> M3)

## Goal
Ship a personalized, stable desktop pet fork based on `Cinquain-Xy/DyberPet` with a safe release process.

## Milestones

### M1 (Week 1): Bootstrap & Branding
- [ ] Rename product name (UI text / docs)
- [ ] Replace app icon and branding assets
- [ ] Define first custom pet/mod package scope
- [ ] Freeze Python dependency versions
- [ ] Create release and security checklists

### M2 (Week 2): Stability & Safety
- [ ] Add import validation for mod assets/config
- [ ] Add save backup/recovery workflow
- [ ] Harden file path handling (no traversal)
- [ ] Add structured error logging
- [ ] Smoke test on Windows (required), macOS (optional)

### M3 (Week 3): Release Readiness
- [ ] Build reproducible release artifact
- [ ] Publish SHA256 checksums
- [ ] Draft release notes template
- [ ] Validate upgrade path from previous user data
- [ ] Tag and publish first forked release

## Definition of Done (M1)
- A clean branch with docs, checklists, and actionable tasks.
- Team can start coding tasks without ambiguity.
