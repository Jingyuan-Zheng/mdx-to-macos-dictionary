# MDX to macOS Dictionary Skill

An Agent Skill that converts MDict (`.mdx`) dictionaries into native macOS `.dictionary` bundles, installs them in Dictionary.app, and builds a DMG installer.

## Install

```bash
npx skills add Jingyuan-Zheng/mdx-to-macos-dictionary-skill --agent codex
```

## What it does

- Extracts MDX entries with `mdict-utils`.
- Compiles a searchable Apple Dictionary bundle.
- Uses a supplied book cover or logo as the bundle icon when available.
- Creates a drag-to-install DMG with [dmg-maker](https://github.com/Jingyuan-Zheng/dmg-maker).

## Requirements

macOS, Python 3, Xcode Command Line Tools, Rosetta on Apple Silicon, and Homebrew's `create-dmg`. The skill checks prerequisites before conversion and provides remediation for any missing item.

## External dependencies

The skill automatically obtains these open-source components when they are missing:

- [dmg-maker](https://github.com/Jingyuan-Zheng/dmg-maker) — creates the final drag-to-install DMG.
- [Dictionary Development Kit](https://github.com/SebastianSzturo/Dictionary-Development-Kit) — compiles the native Apple Dictionary bundle.
- [mdict-utils](https://pypi.org/project/mdict-utils/) — extracts entries from MDX dictionaries.

## Usage

Ask a supported coding agent to convert a local `.mdx` file or folder into a macOS Dictionary. It will preserve companion CSS when present and install the result in `~/Library/Dictionaries/` unless asked for an output-only conversion.

## License

MIT.
