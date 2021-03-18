#!/bin/bash

echo "Checking requirements"

/bin/bash ./bin/compile_dependencies.sh

echo "------------------------------------"
echo "----------- Diff command -----------"
echo "------------------------------------"
git diff --exit-code requirements/*.txt
echo "------------------------------------"
echo "----------- End Diff command -----------"
echo "------------------------------------"

# Check if any requirements files have changed
CHANGED=$(git diff --exit-code requirements/*.txt)

if [ -n "$CHANGED" ]; then
    echo "Requirements seem to have been changed.  Please update and re-commit requirements changes"
    exit 1
fi

echo "Done"
