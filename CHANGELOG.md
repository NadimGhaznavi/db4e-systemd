## [1.1.1] - 2025-06-26
- BugFix: Included the updated code (DOH)

## [1.1.0] - 2025-06-26
- Feature: Added enable() to enable startup at boot time
- Feature: Added disable() to disable startup at boot time
These features require sudo access. 

## [1.0.2] - 2025-06-25
- BugFix: status() was calling \_run_systemd() with an extra arg
- BugFix: start() was calling \_run_systemd() with an extra arg
- BugFix: stop() was calling \_run_systemd() with an extra arg

## [1.0.1] - 2025-06-25
### Fixed
- BugFix: __init__ was calling status() with an extra arg
