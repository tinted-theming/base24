# Colors Overview

**Version 0.1.2**

We define a set of color codes organized into shades ranging from dark
to light. These codes are commonly used in software development and
design for creating themes or styling user interfaces.

## Base24 Fallbacks

We provide a mapping between Base24 and Base16 color codes for
reference:

| Base24 | Base16 |
| ------ | ------ |
| `base10` | `base00` |
| `base11` | `base00` |
| `base12` | `base08` |
| `base13` | `base0A` |
| `base14` | `base0B` |
| `base15` | `base0C` |
| `base16` | `base0D` |
| `base17` | `base0E` |

## Usage Guidelines

We offer guidelines for both dark and light themes:

- **Dark Theme**:
  - Colors from `base00` to `base07` should range from dark to light.
  - Colors `base10` to `base11` should span from light to dark, but still
	darker than `base00`.

- **Light Theme**:
  - Colors from `base00` to `base07` should range from light to dark.
  - Colors `base10` to `base11` should span from dark to light, but lighter
    than `base00`.

## Specific Colors and Their Usages

Each color (baseNN) serves a specific purpose or use case, such as
background, foreground, variables, etc.
Here is an overview; additional guidance is provided in the following sections.

| Color                                                  | BaseNN | Ansi | Terminal/Color Use | Text Editor |
| ------------------------------------------------------- | ------ | ---- | ------------------- | ----------- |
| ![Colour](https://placehold.co/25/282c34/000000?text=%2B) | `base00` | 0    | Background          | Default Background |
| ![Colour](https://placehold.co/25/3f4451/000000?text=%2B) | `base01` | 18   | (Darkest Gray)      | Lighter Background (Used for status bars) |
| ![Colour](https://placehold.co/25/4f5666/000000?text=%2B) | `base02` | 19   | Bright Black        | Selection Background |
| ![Colour](https://placehold.co/25/545862/000000?text=%2B) | `base03` | 8    | (Gray)              | Comments, Invisibles, Line Highlighting |
| ![Colour](https://placehold.co/25/9196a1/000000?text=%2B) | `base04` | 20   | (Light Gray)        | Dark Foreground (Used for status bars) |
| ![Colour](https://placehold.co/25/abb2bf/000000?text=%2B) | `base05` | 21   | Foreground          | Default Foreground, Caret, Delimiters, Operators |
| ![Colour](https://placehold.co/25/e6e6e6/000000?text=%2B) | `base06` | 7    | White               | Light Foreground (Not often used) |
| ![Colour](https://placehold.co/25/ffffff/000000?text=%2B) | `base07` | 15   | Bright White        | The Lightest Foreground (Not often used) |
| ![Colour](https://placehold.co/25/e06c75/000000?text=%2B) | `base08` | 1    | Red                 | Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted |
| ![Colour](https://placehold.co/25/d19a66/000000?text=%2B) | `base09` | 16   | (Orange)            | Integers, Boolean, Constants, XML Attributes, Markup Link Url |
| ![Colour](https://placehold.co/25/e5c07b/000000?text=%2B) | `base0A` | 3    | Yellow              | Classes, Markup Bold, Search Text Background |
| ![Colour](https://placehold.co/25/98c379/000000?text=%2B) | `base0B` | 2    | Green               | Strings, Inherited Class, Markup Code, Diff Inserted |
| ![Colour](https://placehold.co/25/56b6c2/000000?text=%2B) | `base0C` | 6    | Cyan                | Support, Regular Expressions, Escape Characters, Markup Quotes |
| ![Colour](https://placehold.co/25/61afef/000000?text=%2B) | `base0D` | 4    | Blue                | Functions, Methods, Attribute IDs, Headings |
| ![Colour](https://placehold.co/25/c678dd/000000?text=%2B) | `base0E` | 5    | Magenta             | Keywords, Storage, Selector, Markup Italic, Diff Changed |
| ![Colour](https://placehold.co/25/be5046/000000?text=%2B) | `base0F` | 17   | (Dark Red or Brown) | Deprecated Highlighting for Methods and Functions, Opening/Closing Embedded Language Tags, e.g., `<?php ?>` |
| ![Colour](https://placehold.co/25/21252b/000000?text=%2B) | `base10` | -    | (Darker Black)      | Darker Background |
| ![Colour](https://placehold.co/25/181a1f/000000?text=%2B) | `base11` | -    | (Darkest Black)     | The Darkest Background |
| ![Colour](https://placehold.co/25/ff7b86/000000?text=%2B) | `base12` | 9    | Bright Red          | NA |
| ![Colour](https://placehold.co/25/efb074/000000?text=%2B) | `base13` | 11   | Bright Yellow       | NA |
| ![Colour](https://placehold.co/25/b1e18b/000000?text=%2B) | `base14` | 10   | Bright Green        | NA |
| ![Colour](https://placehold.co/25/63d4e0/000000?text=%2B) | `base15` | 14   | Bright Cyan         | NA |
| ![Colour](https://placehold.co/25/67cdff/000000?text=%2B) | `base16` | 12   | Bright Blue         | NA |
| ![Colour](https://placehold.co/25/e48bff/000000?text=%2B) | `base17` | 13   | Bright Magenta      | NA |

Note: The colors `base00` through `base05` are typically neutral.
The colors from `base08` and up are typically more colorful,
and give the color scheme a distinctive "look".

Note: Items in parenthesis for the Terminal/Color Use do not have an
identified terminal use and are a more generic color description.
Implementation may vary depending on the Base24 scheme.

Note: **Bright** colors can have a higher luminosity relative to its
non-bright counterpart. Conventionally, the luminosity can be determined by
looking at the `L` value in the `HSL` color space (for the best accuracy,
[`OKHSL`/`OKHSV`](https://bottosson.github.io/misc/colorpicker) is recommended).
Bright colors can also have increased saturation for stronger emphasis, but this
is not a hard requirement.

![Red and Bright Red Example](https://github.com/tinted-theming/base24/blob/main/assets/red-and-bright-red-example.png?raw=true)
![Red and Bright Red Grayscale Example](https://github.com/tinted-theming/base24/blob/main/assets/red-and-bright-red-grayscale-example.png?raw=true)

### Normal elements

Ordinary text uses foreground `base05` and background `base00`.
Choose these colors for _high_ legibility, as the user does most of the reading and writing with these colors.

Compositors and display managers:
- Use foreground `base00` and background `base01` or `base05` to label normal unfocused workspaces, clients, and tabs.
- Use `base01` or `base05` for the borders of those elements.

### Focus elements

These colors indicate where the user is currently interacting.

Text editors use foreground `base05` and background `base01` to indicate the current line.

Compositors and display managers:
- Use foreground `base00` and background `base0D` to label focused workspaces, clients, and tabs.
- Use `base05` for the borders of those elements.

### Inactive elements

`base03` is used to indicate that something is not active.

Text editors use this as text foreground for comments.
Ensure that it is legible against the normal background (`base00`).

Compositors and display managers:
- Use foreground `base05` and background `base01` to label inactive workspaces, clients, and tabs
- Use `base01` or `base03` for the borders of those elements.

### Category elements

`base08`, `base09`, `base0A`, `base0B`, `base0C`, `base0D` and `base0E`
are used to distinguish between different kinds of elements.

Text editors use these colors as text foregrounds for syntax highlighting.
Ensure that they are legible against the ordinary background (`base01`).

Compositors use these colors for borders and tabs on windows in a tabbed arrangement.

Analysis apps (e.g., system monitors) use these colors in plots and charts to represent different variables.

### Warning elements

`base0F` is used for elements that provide a warning.

Text editors use this as text foreground for warnings.
Ensure that it is legible against the normal background (`base00`).

### Alert elements

These colors indicate errors, alerts, and anything urgent.

Text editors use `base08` as text foreground for errors.
Ensure that it is legible against the normal background (`base00`).

Compositors and display managers:
- Use foreground `base00` and background `base08` to label urgent workspaces, clients, and tabs.
- Use `base08` for the borders of those elements.

### Menu elements

Normal menu options use `base04` as text foreground and `base00` for the background.

### Selected elements

Currently selected menu options use `base05` or `base06` as text foreground and `base02` for the background.

### Matching elements

In applications where the user can search for text,
`base06` is used as foreground for the matching strings.

Some menus will filter the selections as the user begins typing.
- Use `base06`, `base0D` or `base0E` as foreground for the matching characters in unselected options.
- Use `base0D` as foreground for the matching characters in selected options.

