# Calculator

A simple calculator package.

## Development Setup with uv

```bash
# Install uv if you don't have it already
pip install uv

# Create and activate a virtual environment
uv venv

# Install the package in development mode
uv pip install -e .

# Install development dependencies
uv pip install -e ".[dev]"

# Run tests
uv run pytest
```