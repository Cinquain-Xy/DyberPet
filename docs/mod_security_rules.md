# Mod Security Rules (M1)

## Allowed file types
- `.json`
- `.png`
- `.jpg` / `.jpeg`
- `.wav`
- `.ogg` (optional)

## Rejected by default
- Executables/scripts: `.exe`, `.bat`, `.cmd`, `.ps1`, `.sh`, `.py`
- Unknown extensions
- Hidden/system files

## Path safety
- Reject absolute paths
- Reject `..` traversal segments
- Reject symlink escape from import root

## Size limits (initial suggestion)
- Single file <= 10 MB
- Total package <= 100 MB
- File count <= 2000

## Validation
- JSON must parse successfully
- Required keys must exist (to be defined by schema version)
- Unknown schema version => reject (fail closed)
