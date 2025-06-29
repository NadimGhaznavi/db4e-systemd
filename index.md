---
title: db4e-systemd
layout: default
---

# Introduction

A lightweight Python module to interact with `systemd` services via `systemctl`, designed for use in Python-based service managers, admin tools, and dashboards.

---

# Features

* Query service status, PID, and enablement
* Start, stop, and restart services
* Structured output, clean API
* Parses and interprets `systemctl` output

---

# Installation

```bash
pip install git+https://github.com/NadimGhaznavi/db4esystemd.git
```

Or clone locally:

```bash
git clone https://github.com/NadimGhaznavi/db4esystemd.git
cd db4e-systemd
```

---

# Example Usage

```python
from Db4eSystemd.Db4eSystemd import Db4eSystemd

svc = Db4eSystemd('db4e')

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
svc = Db4eSystemd('myservice')

svc.start()          # Start service
svc.stop()           # Stop service
svc.restart()        # Restart service
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

Created and maintained by Nadim-Daniel Ghaznavi. Part of the [db4e](https://github.com/NadimGhaznavi/db4e) project.

