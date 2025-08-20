## [1.2.3] -2025-08-20
- BugFix: active() wasn't returning the correct value

## [1.2.2] - 2025-06-26
- BugFix: stop() wasn't returning the return code.

## [1.2.1] - 2025-06-26
- BugFix: Included the updated code (double DOH)

## [1.2.0] - 2025-06-26
- BugFix: Fixed clash between method and property (service_name) names.
- Feature: When start(), stop(), enable() or disable() is called, return the returncode.
- BugFix: All sysemctl commands require sudo, except for status.
- Docs: Added additional documention around limiting access with sudo.

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
