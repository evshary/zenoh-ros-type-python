upload:
    # Build packages
    poetry run python3 -m pip install --upgrade build
    poetry run python3 -m build
    # Upload to PyPI
    poetry run python3 -m pip install --upgrade twine
    #poetry run python3 -m twine check dist/*
    poetry run python3 -m twine upload --verbose --skip-existing dist/*

clean:
    rm -rf build dist .venv .ruff_cache zenoh_ros_type.egg-info
