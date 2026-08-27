# Security Baseline (Fork)

## 1) Supply Chain Rules
- Only build from this repository (`Cinquain-Xy/DyberPet`) and trusted upstream commits.
- Do not ship binaries from third-party mirrors.
- Pin dependency versions before release.

## 2) Artifact Integrity
- Publish SHA256 checksums for every release artifact.
- Keep a build log with commit SHA and dependency lock snapshot.

## 3) Runtime Principle: Least Privilege
- No admin privileges required by default.
- Minimize auto-start and background permissions.
- Document all network behavior (if any).

## 4) Mod Import Hardening
- Allowlist file types and maximum file sizes.
- Validate JSON config schema before import.
- Block path traversal (`../`, absolute paths, symlink escapes).
- Import into a dedicated sandbox directory.

## 5) Data Safety
- Version user save schema.
- Backup save before migration.
- Recover automatically from the latest valid backup if parse fails.

## 6) Incident Response
- If suspicious behavior is reported:
  1. Freeze release channel.
  2. Reproduce in clean VM.
  3. Rebuild artifact from known-good commit.
  4. Publish transparency note with timeline and hashes.
