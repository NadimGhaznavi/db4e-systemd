# Introduction

A lightweight Python module to interact with `systemd` services via `systemctl`, designed for use in Python-based service managers, admin tools, and dashboards.

---

# Features

* Query service status, PID, and enablement
* Start, stop, and restart services
* Enable and disable services
* Structured output, clean API
* Parses and interprets `systemctl` output

**IMPORTANT NOTE:** All `systemctl` operations except for `sysemctl status` require root access. This module uses `sudo` to deal with this fact. It's recommended that you use a fine-grained sudo configuration. For example, the following two lines in the `/etc/sudoers` file allow the *sally* user to start and stop the *db4e* services. 

```
sally ALL=(ALL) NOPASSWD: /bin/systemctl start db4e
sally ALL=(ALL) NOPASSWD: /bin/systemctl stop db4e
```

So a script that *sally* runs that uses this module will be successful in starting and stopping the *db4e* service, but will fail if `enable()` or `disable()` are attempted.

---

# Installation

```bash
pip install db4e-systemd
```

Or clone locally:

```bash
git clone https://github.com/NadimGhaznavi/db4esystemd.git
cd db4e-systemd
```

---

# Example Usage

```python
from Db4ESystemD.Db4ESystemD import Db4ESystemD

svc = Db4ESystemD('db4e')

if not svc.installed():
    print("Service not installed")
elif not svc.active():
    print("Service is stopped. Starting...")
    svc.start()
else:
    print(f"Service is running with PID {svc.pid()}")
```

---

# Methods

```python
svc = Db4ESystemD('myservice')

svc.start()          # Start service
svc.stop()           # Stop service
svc.restart()        # Restart service
svc.enable()         # Enable service startup at boot time
svc.disable()        # Disable service startup at boot time
svc.status()         # Refresh status
svc.active()         # True/False
svc.enabled()        # True/False
svc.installed()      # True/False
svc.pid()            # Integer PID or None
svc.stdout()         # Raw systemctl stdout
svc.stderr()         # Raw systemctl stderr
```

---

# License

GPL v3 - See LICENSE.txt

---

Created and maintained by Nadim-Daniel Ghaznavi. Part of the [Database 4 Everything](https://github.com/NadimGhaznavi/db4e) project.

