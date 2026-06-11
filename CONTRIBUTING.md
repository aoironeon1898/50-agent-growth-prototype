# Contribution Guidelines

## Development Setup
```bash
git clone https://github.com/aoironeon1898/50-agent-growth-prototype
cd 50-agent-growth-prototype
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -e .
pip install pytest
```

## Testing
```bash
pytest -v
```

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes and test locally
3. Commit with Copilot trailer:
   ```
   git commit -m "Your message
   
   Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
   ```
4. Push and create PR against `main`
5. Ensure CI passes (pytest)
6. Request review before merge

## Code Style

- Python 3.8+
- Use docstrings for public functions
- Minimal comments; self-documenting code preferred
- Type hints encouraged

## Adding a New Growth Strategy

1. Extend `IntelligentGrowthEngine` or `GuardedGrowthEngine`
2. Override `grow_with_strategy()` or `grow_generation()`
3. Add tests in `test_advanced.py` or new test file
4. Update README with usage example
5. Submit PR
