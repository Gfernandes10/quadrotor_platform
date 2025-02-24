#!/bin/bash


SUBMODULE_PATH="../MIL/MIL_tello_platform"
SUBMODULE_REPO="git@github.com:Gfernandes10/MIL_tello_platform.git"
echo "Installing tello MIL platform..."
# Check if the submodule is already cloned
if [ -d "$SUBMODULE_PATH" ] && [ "$(ls -A $SUBMODULE_PATH)" ]; then
    echo "Submodule already cloned. Updating..."
    cd "$SUBMODULE_PATH"
    git fetch origin
    git checkout $(git rev-parse HEAD)  # Ensure it's at the correct commit referenced by the main repo
    git pull origin $(git rev-parse --abbrev-ref HEAD)  # Pull latest changes if on a trackable branch
    cd ..
else
    echo "Submodule not found or empty. Cloning..."
    git submodule update --init --recursive
fi

echo "Submodule updated successfully!"
