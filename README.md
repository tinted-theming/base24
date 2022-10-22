# Tinted Theming: all your themes, everywhere.
<img alt="Color wheel" src="./color_wheel.png" width="100" align="right" style="padding-top:0.6rem;">

 Style systems and smart build tooling for crafting high fidelity color schemes and easily using them in all your favorite apps.  Originally based on the amazing work of [Chris Kempson](https://github.com/chriskempson/) and his [Base16](https://github.com/chriskempson/base16) system.


- [Tinted Theming: all your themes, everywhere.](#tinted-theming-all-your-themes-everywhere)
	- [Features](#features)
	- [Base24 Compatibility](#base24-compatibility)
	- [Documentation and Specification](#documentation-and-specification)
		- [Scheme](#scheme)
		- [Style](#style)
		- [Builder](#builder)
		- [Template](#template)
	- [Supported Applications (Base24)](#supported-applications-base24)
		- [Existing Base16 Templates (Base16)](#existing-base16-templates-base16)
	- [Scheme Repositories](#scheme-repositories)
		- [Generated from existing themes](#generated-from-existing-themes)
		- [Existing Base16 Schemes](#existing-base16-schemes)
	- [Builder Repositories](#builder-repositories)
	- [Download](#download)
		- [Clone](#clone)
			- [Using The Command Line](#using-the-command-line)
			- [Using GitHub Desktop](#using-github-desktop)
		- [Download Zip File](#download-zip-file)
	- [Community](#community)
		- [Licence](#licence)
		- [Changelog](#changelog)
		- [Project Chat](#project-chat)
		- [Credits](#credits)

## Features

- Seamless builder support for _multiple_ style systems ([Base16](https://github.com/chriskempson/base16), [Base17](https://github.com/tinted-theming/base17), [Base24](https://github.com/tinted-theming/base24/), [BaseNext DRAFT](https://github.com/tinted-theming/basenext), etc.)
- Over 230 beautiful and ready-to-use color schemes. [View the Gallery](https://tinted-theming.github.io/base16-gallery).
- Over 70 supported GUI and terminal applications. [See the full list](#supported-applications-base24).
- Allows end users to choose a color scheme and know it will be available _everywhere_.
- Allows color scheme designers to craft a palette of colors once, instantly supporting for many different apps.

## Base24 Compatibility
The aim of this project is to offer compatibility with base16. The only
limitation is that a base24 builder is needed for base24 templates.

|Theme|⇒|Template|Base16 Builder|Base24 Builder|
|---|---|---|---|---|
|Base16|⇒|Base16|:heavy_check_mark:|:heavy_check_mark:|
|Base24|⇒|Base16|:heavy_check_mark:|:heavy_check_mark:|
|Base16|⇒|Base24|:x:|:heavy_check_mark:|
|Base24|⇒|Base24|:x:|:heavy_check_mark:|

## Documentation and Specification

The _builder_ and _styling_ specs detail how to compile _schemes_ and _templates_ into application specific configurations.

### Scheme

A scheme is a fixed palette of named colors and (optionally) instructions for how those colors should be used by apps.

### Style

A style guide provides rules governing how a scheme's palette should be applied within apps.  This means each color is used consistently for similar purposes across all your apps.  Individual styling guides often support different sized pallets and have different ideas about how those colors should be deployed.

See the individual styling guides for more information on each:

- [Base16](https://github.com/tinted-theming/home/blob/main/styling.md) - the original, 16 colors with very fixed semantic meanings.
- [Base17](https://github.com/tinted-theming/base17/blob/main/styling.md) - our evolution of Base16. It's still 16 colors, but far more power and flexibility to create higher fidelity themes and templates.
- [Base24](https://github.com/tinted-theming/base24/blob/master/styling.md) **Hey that's this repo!** - an extra 8  colors for full ANSI support in your terminals.
- [BaseNext DRAFT](https://github.com/tinted-theming/basenext) - as many colors as you want, along with the flexibility and complexity.

A scheme is defined using a [YAML](https://yaml.org/) file. The file specification is in the [Builder Guidelines](/builder.md#schemes-repository).

### Builder

A builder is a build tool used by various template repositories to generate files based on scheme file and template file.

- [Builder Guidelines](/builder.md)

### Template

A template describes how a scheme should be transformed to support a specific application.  A template repository defines a template file, then uses a builder to generate application specific files using the template.

Templates often include ready-to-use pre-built versions of every scheme. These are typically installed directly by end users to use the schemes in different applications.

## Supported Applications (Base24)

To add your own template, submit a pull request to URL and add your repository to the list below. **Repository naming scheme: base24-\[template-name\]** (with dashes as separators).

- [CSS etc](https://github.com/Base24/base24-css-etc)
- [Gnome Terminal](https://github.com/Base24/base24-gnome-terminal)
- [HTML](https://github.com/Base24/base24-html)
- [iTerm2](https://github.com/Base24/base24-iterm2)
- [Kate](https://github.com/Base24/base24-kate)
- [KDEPlasma](https://github.com/Base24/base24-kdeplasma)
- [Kitty](https://github.com/Base24/base24-kitty-te)
- [Konsole](https://github.com/Base24/base24-konsole)
- [PuTTY](https://github.com/Base24/base24-putty)
- [Slack](https://github.com/Base24/base24-slack)
- [Termux](https://github.com/Base24/base24-termux)
- [VSCode](https://github.com/Base24/base24-vscode)
- [VSCode Terminal](https://github.com/Base24/base24-vscode-terminal)
- [Windows Terminal](https://github.com/Base24/base24-windows-terminal)
- [XFCE4 Terminal](https://github.com/Base24/base24-xfce4-terminal)

### Existing Base16 Templates (Base16)

- [Alacritty](https://github.com/aaron-williamson/base16-alacritty)
- [Binary Ninja](https://github.com/evanrichter/base16-binary-ninja)
- [Blink](https://github.com/niklaas/base16-blink)
- [C Header](https://github.com/m1sports20/base16-c_header)
- [ConCfg](https://github.com/h404bi/base16-concfg)
- [ConEmu](https://github.com/martinlindhe/base16-conemu)
- [Console2](https://github.com/AFulgens/base16-console2)
- [ConsoleZ](https://github.com/AFulgens/base16-consolez)
- [Crosh](https://github.com/philj56/base16-crosh)
- [Dunst](https://github.com/khamer/base16-dunst)
- [dwm](https://github.com/dgmulf/base16-dwm)
- [Emacs](https://github.com/belak/base16-emacs)
- [everything](https://github.com/spitfire05/base16-everything)
- [fzf](https://github.com/fnune/base16-fzf)
- [Godot](https://github.com/Calinou/base16-godot)
- [gtk-flatcolor](https://github.com/Misterio77/base16-gtk-flatcolor)
- [GTK+2](https://github.com/dawikur/base16-gtk2)
- [Highlight](https://github.com/bezhermoso/base16-highlight)
- [i3](https://github.com/khamer/base16-i3)
- [i3status](https://github.com/Eluminae/base16-i3status)
- [i3status-rust](https://github.com/mystfox/base16-i3status-rust)
- [Jetbrains](https://github.com/adilosa/base16-jetbrains)
- [JOE](https://github.com/jjjordan/base16-joe)
- [Kakoune](https://github.com/leira/base16-kakoune)
- [luakit](https://github.com/twnaing/base16-luakit)
- [mako](https://github.com/Eluminae/base16-mako)
- [MinTTY](https://github.com/geoffstokes/base16-mintty)
- [MonoDevelop](https://github.com/netpyoung/base16-monodevelop)
- [Prism](https://github.com/atelierbram/base16-prism)
- [prompt-toolkit & ipython](https://github.com/memeplex/base16-prompt-toolkit)
- [Pygments](https://github.com/mohd-akram/base16-pygments)
- [QOwnNotes](https://github.com/themix-project/base16-template-qOwnNotes)
- [Qt Creator](https://github.com/ilpianista/base16-qtcreator)
- [qutebrowser](https://github.com/theova/base16-qutebrowser)
- [Rofi](https://gitlab.com/0xdec/base16-rofi)
- [Scide](https://github.com/brunoro/base16-scide)
- [Shell](https://github.com/tinted-theming/base16-shell)
- [st](https://github.com/dgmulf/base16-st)
- [StumpWM](https://github.com/tpine/base16-stumpwm)
- [Sway](https://github.com/rkubosz/base16-sway)
- [terminator](https://github.com/Schnouki/base16-terminator)
- [Termite](https://github.com/khamer/base16-termite)
- [textadept](https://github.com/rgieseke/base16-textadept)
- [TextMate & Sublime Text](https://github.com/chriskempson/base16-textmate)
- [Tilix](https://github.com/karlding/base16-tilix)
- [vim-airline-themes](https://github.com/dawikur/base16-vim-airline-themes)
- [Vim](https://github.com/tinted-theming/base16-vim)
- [vimiv](https://github.com/karlch/base16-vimiv)
- [Vis](https://github.com/pshevtsov/base16-vis)
- [Waybar](https://github.com/mnussbaum/base16-waybar)
- [Windows Command Prompt](https://github.com/iamthad/base16-windows-command-prompt)
- [Xcode](https://github.com/kreeger/base16-xcode)
- [Xresources](https://github.com/binaryplease/base16-xresources)
- [Xshell](https://github.com/h404bi/base16-xshell)
- [zathura](https://github.com/nicodebo/base16-zathura)

## Scheme Repositories

To add your own scheme, submit a pull request to URL and add your repository to the list below. **Repository naming scheme: base24-\[scheme-name\]-scheme** (with dashes as separators).

- [Brogrammer](https://github.com/Base24/base24-brogrammer-scheme)
- [Dracula24](https://github.com/Base24/base24-dracula-scheme)
- [Espresso](https://github.com/Base24/base24-espresso-scheme)
- [Framer](https://github.com/Base24/base24-framer-scheme)
- [Github](https://github.com/Base24/base24-github-scheme)
- [One Black](https://github.com/Base24/base24-one-black-scheme)
- [One Dark](https://github.com/Base24/base24-one-dark-scheme)
- [One Light](https://github.com/Base24/base24-one-light-scheme)

### Generated from existing themes

- [Generated from Iterm2 themes](https://github.com/Base24/base24-mbadolato-iterm2-color-schemes)

### Existing Base16 Schemes

- [Atelier](https://github.com/atelierbram/base16-atelier-schemes)
- [Atlas](https://github.com/ajlende/base16-atlas-scheme)
- [Black Metal](https://github.com/metalelf0/base16-black-metal-scheme)
- [Brush Trees](https://github.com/whiteabelincoln/base16-brushtrees-scheme)
- [Circus](https://github.com/stepchowfun/base16-circus-scheme)
- [Classic](https://github.com/detly/base16-classic-scheme)
- [Codeschool](https://github.com/blockloop/base16-codeschool-scheme)
- [colors](https://github.com/hakatashi/base16-colors-scheme)
- [Cupertino](https://github.com/Defman21/base16-cupertino)
- [darkmoss](https://github.com/avanzzzi/base16-darkmoss-scheme)
- [darkviolet](https://github.com/ruler501/base16-darkviolet-scheme)
- [Default](https://github.com/chriskempson/base16-default-scheme)
- [dirtysea](https://github.com/tartansandal/base16-dirtysea-scheme)
- [edge](https://github.com/cjayross/base16-edge-schemes)
- [equilibrium](https://github.com/carloabelli/base16-equilibrium-scheme)
- [eva](https://github.com/kjakapat/base16-eva-scheme)
- [Fruit Soda](https://github.com/jozip/base16-fruit-soda-scheme)
- [Gruvbox](https://github.com/dawikur/base16-gruvbox-scheme)
- [Hardcore](https://github.com/callerc1/base16-hardcore-scheme)
- [Helios](https://github.com/reyemxela/base16-helios-scheme)
- [Heetch](https://github.com/tealeg/base16-heetch-scheme)
- [Horizon](https://github.com/michael-ball/base16-horizon-scheme)
- [humanoid](https://github.com/humanoid-colors/base16-humanoid-schemes)
- [iA](https://github.com/aramisgithub/base16-ia-scheme)
- [Icy](https://github.com/icyphox/base16-icy-scheme)
- [Materia](https://github.com/Defman21/base16-materia)
- [Material Theme](https://github.com/ntpeters/base16-materialtheme-scheme)
- [Material Vivid](https://github.com/joshyrobot/base16-material-vivid-scheme)
- [Mellow](https://github.com/gidsi/base16-mellow-scheme)
- [Mexico-Light](https://github.com/drzel/base16-mexico-light-scheme)
- [nebula](https://github.com/Misterio77/base16-nebula-scheme)
- [nord](https://github.com/spejamchr/base16-nord-scheme)
- [Nova](https://github.com/gessig/base16-nova-scheme)
- [Outrun](https://github.com/hugodelahousse/base16-outrun-schemes)
- [PaperColor](https://github.com/jonleopard/base16-papercolor-scheme)
- [pasque](https://github.com/Misterio77/base16-pasque-scheme)
- [Porple](https://github.com/AuditeMarlow/base16-porple-scheme)
- [Purpledream](https://github.com/archmalet/base16-purpledream-scheme)
- [Rebecca](https://github.com/vic/base16-rebecca)
- [Sandcastle](https://github.com/gessig/base16-sandcastle-scheme)
- [Snazzy](https://github.com/h404bi/base16-snazzy-scheme)
- [Solarflare](https://github.com/mnussbaum/base16-solarflare-scheme)
- [Solarized](https://github.com/aramisgithub/base16-solarized-scheme)
- [Summercamp](https://github.com/zoefiri/base16-summercamp)
- [Summerfruit](https://github.com/cscorley/base16-summerfruit-scheme)
- [Synth Midnight](https://github.com/michael-ball/base16-synth-midnight-scheme)
- [tango](https://github.com/Schnouki/base16-tango-scheme)
- [Tomorrow](https://github.com/chriskempson/base16-tomorrow-scheme)
- [Twilight](https://github.com/hartbit/base16-twilight-scheme)
- [Unikitty](https://github.com/joshwlewis/base16-unikitty)
- [vice](https://github.com/Thomashighbaugh/base16-vice-scheme)
- [vulcan](https://github.com/andreyvpng/base16-vulcan-scheme)
- [Woodland](https://github.com/jcornwall/base16-woodland-scheme)
- [Zenburn](https://github.com/elnawe/base16-zenburn-scheme)
- [XCode Dust](https://github.com/gonsie/base16-xcode-dusk-scheme)
- [Old Unclaimed Schemes](https://github.com/chriskempson/base16-unclaimed-schemes) - If your scheme is in this repository, please give it a new home!

## Builder Repositories

**Repository naming scheme: base24-builder-\[language\]** (with dashes as separators). The separate headings are the latest versions of the spec supported by each builder.

## Download

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2

```bash
git clone https://github.com/tinted-theming/Base24
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community

### Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Project Chat

Have something you want to discuss, but you're not sure it warrants an issue? Feel free to stop by the [#base16 channel](https://web.libera.chat/#base16) on [Libera Chat](https://libera.chat/) or the [bridged Matrix channel](https://matrix.to/#/#base16:libera.chat) to talk about it.

### Credits

- Thanks to [Chris Kempson](https://github.com/chriskempson) for the original concept and implementation.
- Color wheel icon thanks to [Color icons created by Nikita Golubev - Flaticon](https://www.flaticon.com/free-icons/color).
