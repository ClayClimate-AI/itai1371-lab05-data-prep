#!/usr/bin/env python3
import importlib
import sys

REQUIRED = ["pandas", "numpy", "matplotlib", "seaborn", "sklearn"]

def main() -> int:
    missing = []
    for name in REQUIRED:
        mod = "sklearn" if name == "sklearn" else name
        try:
            importlib.import_module(mod)
        except ImportError:
            missing.append(name)
    if missing:
        print("FAIL missing:", ", ".join(missing))
        return 1
    print("OK Lab 05 environment gate passed")
    print("Python", sys.version.split()[0])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
