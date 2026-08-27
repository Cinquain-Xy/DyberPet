# Mod Schema Plan

## Objective
Define a strict schema for pet/mod packages to reduce crash and injection risks.

## Validation Layers
1. **Manifest-level**
   - Required keys: `name`, `version`, `author`, `assets`, `actions`
   - Semantic version format for `version`

2. **Asset-level**
   - Allowed extensions (e.g. `.png`, `.json`, `.wav`)
   - Max asset count and per-file size limit
   - Reject hidden files and executable payloads

3. **Path-level**
   - Normalize path and reject traversal
   - No absolute paths
   - No symlink escaping

4. **Action-level**
   - Validate referenced animation/action names exist
   - Validate numeric ranges (speed, scale, intervals)

## Error Policy
- Fail closed: any validation error aborts import.
- Return user-facing concise message + detailed internal log.

## Next Steps
- [ ] Select validation library (or custom validator)
- [ ] Add `schema_version`
- [ ] Create sample valid/invalid fixtures
- [ ] Add unit tests for importer
