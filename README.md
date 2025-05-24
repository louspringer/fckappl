# fckappl

> ⚠️ **ALPHA NOTICE**: This project is in early setup. It is non-functional and exploratory. Use at your own risk — or wait a bit.

> A package to mitigate macOS's annoying habit of flipping configuration switches unnecessarily.  
> Use this if your last known good is better than Apple's erroneous and disruptive last known good.

**fckappl** is a command-line scaffold for future tooling meant to help users recover from spontaneous macOS preference reversals — the kind that quietly unset Universal Control, change AirPlay routing, or unpair Bluetooth devices overnight.

We don’t hate Apple — we just hate re-clicking the same toggles. This project exists as a clean, expandable CLI baseline to automate those restorations once the right mechanisms are identified.

Right now, it’s just getting set up — but it’s built right.

## ✅ Features

- Python 3.10+ CLI project using [`uv`](https://github.com/astral-sh/uv)
- `src/` layout (clean install path, avoids import bleed)
- Typer-based CLI scaffolding
- Stubbed `init` and `run` commands (emit “unimplemented”)
- RDF ontology (`fckappl-ontology.ttl`) documenting what, why, and how

## 🚀 Installation

```bash
uv venv .venv --python=python3.10
source .venv/bin/activate
uv pip install -e .
