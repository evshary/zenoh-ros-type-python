upload:
    # Clean old artifacts
    rm -rf dist
    # Build
    uv run --with build python -m build
    # Upload
    #uv run --with twine python3 -m twine check dist/*
    uv run --with twine python -m twine upload --verbose --skip-existing dist/*

test:
    uv sync --extra dev
    uv run pytest tests

clean:
    rm -rf build dist .venv .ruff_cache zenoh_ros_type.egg-info
