#!/usr/bin/env python3
"""Run all examples"""

import importlib.util
import sys
from pathlib import Path

examples_dir = Path(__file__).parent

for example_file in sorted(examples_dir.glob("example_*.py")):
    if example_file.name == "run_examples.py":
        continue
    
    spec = importlib.util.spec_from_file_location(
        example_file.stem, 
        str(example_file)
    )
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f"Error running {example_file.name}: {e}")
        sys.exit(1)
