# Colours Overview

**Version 0.1.0**

We define a set of colour codes organized into shades ranging from dark
to light. These codes are commonly used in software development and
design for creating themes or styling user interfaces.

## Base24 Fallbacks

We provide a mapping between Base24 and Base16 colour codes for
reference:

| Base24 | Base16 |
| ------ | ------ |
| base10 | base00 |
| base11 | base00 |
| base12 | base08 |
| base13 | base0A |
| base14 | base0B |
| base15 | base0C |
| base16 | base0D |
| base17 | base0E |

## Usage Guidelines

We offer guidelines for both dark and light themes:

- **Dark Theme**:
  - Colours from base00 to base07 should range from dark to light.
  - Colours base10 to base11 should span from light to dark, but still
	darker than base00.

- **Light Theme**:
  - Colours from base00 to base07 should range from light to dark.
  - Colours base10 to base11 should span from dark to light, but lighter
    than base00.

## Specific Colours and Their Usages

Each colour (baseNN) serves a specific purpose or use case, such as
background, foreground, variables, etc. Here's a breakdown:

| Colour                                                  | BaseNN | Ansi | Terminal/Colour Use | Text Editor |
| ------------------------------------------------------- | ------ | ---- | ------------------- | ----------- |
| ![Colour](https://placehold.it/25/282c34/000000?text=+) | base00 | -    | Background          | Default Background |
| ![Colour](https://placehold.it/25/3f4451/000000?text=+) | base01 | 0    | Black               | Lighter Background (Used for status bars) |
| ![Colour](https://placehold.it/25/4f5666/000000?text=+) | base02 | 8    | Bright Black        | Selection Background |
| ![Colour](https://placehold.it/25/545862/000000?text=+) | base03 | -    | (Grey)              | Comments, Invisibles, Line Highlighting |
| ![Colour](https://placehold.it/25/9196a1/000000?text=+) | base04 | -    | (Light Grey)        | Dark Foreground (Used for status bars) |
| ![Colour](https://placehold.it/25/abb2bf/000000?text=+) | base05 | -    | Foreground          | Default Foreground, Caret, Delimiters, Operators |
| ![Colour](https://placehold.it/25/e6e6e6/000000?text=+) | base06 | 7    | White               | Light Foreground (Not often used) |
| ![Colour](https://placehold.it/25/ffffff/000000?text=+) | base07 | 15   | Bright White        | The Lightest Foreground (Not often used) |
| ![Colour](https://placehold.it/25/e06c75/000000?text=+) | base08 | 1    | Red                 | Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted |
| ![Colour](https://placehold.it/25/d19a66/000000?text=+) | base09 | ~3   | (Orange)            | Integers, Boolean, Constants, XML Attributes, Markup Link Url |
| ![Colour](https://placehold.it/25/e5c07b/000000?text=+) | base0A | 3    | Yellow              | Classes, Markup Bold, Search Text Background |
| ![Colour](https://placehold.it/25/98c379/000000?text=+) | base0B | 2    | Green               | Strings, Inherited Class, Markup Code, Diff Inserted |
| ![Colour](https://placehold.it/25/56b6c2/000000?text=+) | base0C | 6    | Cyan                | Support, Regular Expressions, Escape Characters, Markup Quotes |
| ![Colour](https://placehold.it/25/61afef/000000?text=+) | base0D | 4    | Blue                | Functions, Methods, Attribute IDs, Headings |
| ![Colour](https://placehold.it/25/c678dd/000000?text=+) | base0E | 5    | Purple              | Keywords, Storage, Selector, Markup Italic, Diff Changed |
| ![Colour](https://placehold.it/25/be5046/000000?text=+) | base0F | -    | (Dark Red or Brown) | Deprecated Highlighting for Methods and Functions, Opening/Closing Embedded Language Tags, e.g., `<?php ?>` |
| ![Colour](https://placehold.it/25/21252b/000000?text=+) | base10 | -    | (Darker Black)      | Darker Background |
| ![Colour](https://placehold.it/25/181a1f/000000?text=+) | base11 | -    | (Darkest Black)     | The Darkest Background |
| ![Colour](https://placehold.it/25/ff7b86/000000?text=+) | base12 | 9    | Bright Red          | NA |
| ![Colour](https://placehold.it/25/efb074/000000?text=+) | base13 | 11   | Bright Yellow       | NA |
| ![Colour](https://placehold.it/25/b1e18b/000000?text=+) | base14 | 10   | Bright Green        | NA |
| ![Colour](https://placehold.it/25/63d4e0/000000?text=+) | base15 | 14   | Bright Cyan         | NA |
| ![Colour](https://placehold.it/25/67cdff/000000?text=+) | base16 | 12   | Bright Blue         | NA |
| ![Colour](https://placehold.it/25/e48bff/000000?text=+) | base17 | 13   | Bright Purple       | NA |

Note: Items in parenthesis for the Terminal/Colour Use do not have an
identified terminal use and are a more generic colour description.
Implementation may vary depending on the Base24 scheme.

Note: **Bright** colors should have a higher luminosity relative to its
non-bright counterpart. Conventionally, the luminosity can be determined by
looking at the `L` value in the `HSL` color space (for the best accuracy,
[`OKHSL`/`OKHSV`](https://bottosson.github.io/misc/colorpicker) is recommended).
Bright colors can also have increased saturation for stronger emphasis, but this
is not a hard requirement.

![Red and Bright Red Example](https://github.com/tinted-theming/base24/blob/main/assets/red-and-bright-red-example.png?raw=true)
![Red and Bright Red Grayscale Example](https://github.com/tinted-theming/base24/blob/main/assets/red-and-bright-red-grayscale-example.png?raw=true)
