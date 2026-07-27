# MDX to macOS Dictionary

An Agent Skill that converts MDict (`.mdx`) dictionaries into native macOS `.dictionary` bundles, installs them in Dictionary.app, and builds a DMG installer.

## Install

```bash
npx skills add Jingyuan-Zheng/mdx-to-macos-dictionary --agent codex
```

## What it does

- Extracts MDX entries with `mdict-utils`.
- Compiles a searchable Apple Dictionary bundle.
- Uses a supplied book cover or logo as the bundle icon when available.
- Creates a drag-to-install DMG with [dmg-maker](https://github.com/Jingyuan-Zheng/dmg-maker).

## Requirements

macOS, Python 3, Xcode Command Line Tools, Rosetta on Apple Silicon, and Homebrew's `create-dmg`. The skill checks prerequisites before conversion and provides remediation for any missing item.

## Usage

Ask a supported coding agent to convert a local `.mdx` file or folder into a macOS Dictionary. It will preserve companion CSS when present and install the result in `~/Library/Dictionaries/` unless asked for an output-only conversion.

## License

MIT.
