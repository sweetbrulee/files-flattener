#!/bin/bash

# Check if the PYPI_API_TOKEN environment variable is set
if [ -z "$PYPI_API_TOKEN" ]; then
  echo "Error: PYPI_API_TOKEN environment variable is not set."
  exit 1
fi

# Use twine to upload the package
twine upload --username __token__ --password "$PYPI_API_TOKEN" dist/*