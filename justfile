upload:
    # Install package
    python3 -m pip install twine setuptools
    # Upload to PyPI
    python3 setup.py sdist bdist_wheel
    twine upload --verbose --skip-existing dist/*

clean:
    rm -rf build dist .venv .ruff_cache zenoh_ros_type.egg-info
