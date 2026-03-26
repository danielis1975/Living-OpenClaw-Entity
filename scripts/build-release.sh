#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"
VERSION_TAG="${1:-$(date -u +%Y%m%d-%H%M)}"
OUT_TGZ="$DIST_DIR/symbiotic-openclaw-agent-${VERSION_TAG}.tar.gz"

mkdir -p "$DIST_DIR"

# Keep build reproducible and clean from git internals/local artifacts.
tar \
  --exclude='.git' \
  --exclude='dist' \
  --exclude='*.pyc' \
  --exclude='__pycache__' \
  -czf "$OUT_TGZ" \
  -C "$ROOT_DIR" .

echo "$OUT_TGZ"
