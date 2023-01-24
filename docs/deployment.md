# Deployment

To deploy and publish a new version to PyPI, follow these steps:

1. Update the library version in `setup.py` file.
2. Run `python setup.py sdist bdist_wheel` to build the package.
3. Run `twine upload dist/*` to publish the package.
