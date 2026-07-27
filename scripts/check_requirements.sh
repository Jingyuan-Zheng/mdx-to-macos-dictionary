#!/bin/sh
# Check the local prerequisites for producing a native macOS Dictionary DMG.

set -u

missing=0

need_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "MISSING: $1 — $2"
    missing=1
  fi
}

need_command git "Install Xcode Command Line Tools: xcode-select --install"
need_command python3 "Install Python 3, then rerun this check."
need_command xmllint "Install Xcode Command Line Tools: xcode-select --install"
need_command xsltproc "Install Xcode Command Line Tools: xcode-select --install"
need_command plutil "This must run on macOS."
need_command sips "This must run on macOS."
need_command iconutil "This must run on macOS."
need_command ditto "This must run on macOS."

if ! command -v mdict >/dev/null 2>&1; then
  echo "MISSING: mdict — create <work>/mdict-venv and install mdict-utils with pip."
  missing=1
fi

if ! command -v create-dmg >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "MISSING: create-dmg — install with: brew install create-dmg"
  else
    echo "MISSING: create-dmg and Homebrew — install Homebrew, then run: brew install create-dmg"
  fi
  missing=1
fi

if [ "$(uname -m)" = "arm64" ] && ! arch -x86_64 /usr/bin/true >/dev/null 2>&1; then
  echo "MISSING: Rosetta — install with: softwareupdate --install-rosetta --agree-to-license"
  missing=1
fi

if [ "$missing" -ne 0 ]; then
  exit 1
fi

echo "All MDX-to-macOS-Dictionary prerequisites are available."
