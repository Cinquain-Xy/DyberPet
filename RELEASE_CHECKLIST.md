# Release Checklist

## Pre-Build
- [ ] Confirm target commit SHA
- [ ] Confirm dependency versions are pinned
- [ ] Run lint/tests/smoke checks
- [ ] Validate mod import safety checks

## Build
- [ ] Build from clean environment
- [ ] Record Python version and OS build info
- [ ] Generate artifacts

## Verification
- [ ] Run app startup smoke test
- [ ] Test core interactions (drag, click, menu, settings)
- [ ] Test save/load and backup restore
- [ ] Compute SHA256 for each artifact

## Publishing
- [ ] Draft release notes (features/fixes/breaking changes)
- [ ] Attach artifacts + SHA256SUMS
- [ ] Mention license and source changes
- [ ] Link known issues and rollback plan
