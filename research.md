In extending the base16 style guide beyond terminals and text editors, I wanted to be consistent with current practice.
Therefore, I tried to look at representative templates for application launchers, bars (e.g. waybar), and compositors (e.g. sway).
Unfortunately; there aren't many complete templates available for these types of tools.
(By complete, I mean a template that assigns colours to roles,
not one that just defines colour variables and relies on the user
to associate those variables with application settings.)

I didn't address colours for scrollbars.

For future reference and discussion, here's a summary of my research.

## Normal background

- Haze-sh/base16-bemenu: base00
- dark-beep-boop/base16-fuzzel: base00
- aarowill/base16-alacritty: base00

## Normal foreground (text)

- Haze-sh/base16-bemenu: base04
- dark-beep-boop/base16-fuzzel: base05
- aarowill/base16-alacritty: base05

## Normal border

- afistfullofash/base16-stumpwm: base03? base00?
- tinted-theming/base16-i3: base05 (active workspace)
- tinted-theming/base16-i3: base01 (unfocused client)
- rkubosz/base16-sway: base05 (active workspace)
- rkubosz/base16-sway: base01 (unfocused client)

## Title background

- Haze-sh/base16-bemenu: base03

## Title text foreground (tabs, top border)

- Haze-sh/base16-bemenu: base06
- afistfullofash/base16-stumpwm: base04?
- tinted-theming/base16-i3: base00 (active workspace)
- rkubosz/base16-sway: base00 (active workspace)

## Focused background

- afistfullofash/base16-stumpwm: base04?
- tinted-theming/base16-i3: base0D (workspace and client)
- rkubosz/base16-sway: base0D

## Focused foreground (text)

- tinted-theming/base16-i3: base00 (workspace and client)
- rkubosz/base16-sway: base00 (workspace and client)

## Focused border

- afistfullofash/base16-stumpwm: base04?
- tinted-theming/base16-i3: base05 (workspace and client)
- rkubosz/base16-sway: base05 (workspace and client)

## inactive background

- tinted-theming/base16-i3: base01 (workspace and client)
- rkubosz/base16-sway: base01 (workspace and client)

## inactive foreground (text)

- tinted-theming/base16-i3: base05 (workspace and client)
- rkubosz/base16-sway: base05 (workspace and client)

## inactive border

- tinted-theming/base16-i3: base01 (client)
- tinted-theming/base16-i3: base03 (workspace)
- rkubosz/base16-sway: base01 (client)
- rkubosz/base16-sway: base03 (workspace)

## warning foreground

- tinted-theming/base16-emacs: base09

## urgent background

- tinted-theming/base16-i3: base08 (workspace and client)
- rkubosz/base16-sway: base08 (workspace and client)

## urgent foreground (text)

- tinted-theming/base16-i3: base00 (workspace and client)
- rkubosz/base16-sway: base00 (workspace and client)
- tinted-theming/base16-emacs: base08

## urgent border

- tinted-theming/base16-i3: base08 (workspace and client)
- rkubosz/base16-sway: base08 (workspace and client)

## Cursor foreground (text)

Usually the same as normal text foreground

## Selected background

- Haze-sh/base16-bemenu: base02
- dark-beep-boop/base16-fuzzel: base03
- I prefer base02

## Selected foreground (text)

- Haze-sh/base16-bemenu: base0A
- dark-beep-boop/base16-fuzzel: base06
- I like base05

## Filter background

- Haze-sh/base16-bemenu: base00

## Filter foreground (text)

- Haze-sh/base16-bemenu: base06

## Highlighted background

- Haze-sh/base16-bemenu: base02

## Highlighted foreground (text)

- Haze-sh/base16-bemenu: base0A

## Scrollbar background

- Haze-sh/base16-bemenu: base00

## Scrollbar foreground (text)

- Haze-sh/base16-bemenu: base0E

## Matching text foreground (text)

- dark-beep-boop/base16-fuzzel: base0D

## Matching text foreground (text) within a selection

- dark-beep-boop/base16-fuzzel: base0D

## visited links

## distinguishing foreground colours

- tinted-theming/base16-emacs: base09, base0A, base0B, base0D, base0E

## comment foreground (text)

- tinted-theming/base16-emacs: base03


