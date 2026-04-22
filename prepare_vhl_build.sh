#!/bin/bash
set -e

# Repository Root
REPO_ROOT=$(pwd)

echo "Building Runframe Standalone..."
cd "$REPO_ROOT/vhl-webui"
bun install
bun run build:standalone
mkdir -p "$REPO_ROOT/vhl-runtime/dist/runframe"
cp dist/standalone.min.js "$REPO_ROOT/vhl-runtime/dist/runframe/"

echo "Packaging CLI..."
cd "$REPO_ROOT/vhl-cli"
bun install
bun run build
npm pack --pack-destination "$REPO_ROOT/vhl-runtime/dist/"

# Standardize the tarball name for Dockerfile
mv "$REPO_ROOT/vhl-runtime/dist/tscircuit-cli-"*.tgz "$REPO_ROOT/vhl-runtime/dist/tscircuit-cli.tgz"

echo "Artifacts prepared in vhl-runtime/dist/"
echo "You can now run: cd vhl-runtime && docker build -t vhl-runtime ."
