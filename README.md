[![Github top language](https://img.shields.io/github/languages/top/Base24/Base24.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/manual/Base24/Base24)
[![Repository size](https://img.shields.io/github/repo-size/Base24/Base24.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/Base24/Base24.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/Base24/Base24.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/Base24/Base24.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/Base24/Base24.svg?style=for-the-badge)](../../commits/master)

<!-- omit in toc -->
# Base24

<img src="readme-assets/icons/proj-icon.png" alt="Project Icon" width="100">


- [Reason for this repo](#reason-for-this-repo)
- [Compatibility](#compatibility)
- [Why Base24/ Base16 is useful](#why-base24-base16-is-useful)
- [Documentation](#documentation)
- [Template Repositories](#template-repositories)
	- [Existing Base16 Templates](#existing-base16-templates)
- [Scheme Repositories](#scheme-repositories)
	- [Generated from existing themes](#generated-from-existing-themes)
	- [Existing Base16 Schemes](#existing-base16-schemes)
- [Builder Repositories](#builder-repositories)
	- [Base24 0.1.0 (Feb 2020)](#base24-010-feb-2020)
		- [Changes](#changes)
		- [Builders](#builders)
	- [Base16 0.9.1 (Jun 15, 2019)](#base16-091-jun-15-2019)
		- [Changes](#changes-1)
		- [Builders](#builders-1)
- [Download](#download)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)

## Reason for this repo

Base16 doesn't provide bright colours that are used in terminal emulators. e.g.
bright red. Base24 does. In addition to this, Base24 provides darker background
variants. This will also be part of a Github organization.

## Compatibility
The aim of this project is to offer compatibility with base16. The only
limitation is that a base24 builder is needed for base24 templates.

|Theme|⇒|Template|Base16 Builder|Base24 Builder|
|---|---|---|---|---|
|Base16|⇒|Base16|:heavy_check_mark:|:heavy_check_mark:|
|Base24|⇒|Base16|:heavy_check_mark:|:heavy_check_mark:|
|Base16|⇒|Base24|:x:|:heavy_check_mark:|
|Base24|⇒|Base24|:x:|:heavy_check_mark:|


Thank you to https://github.com/chriskempson/base16/ (MIT) for Base16


## Why Base24/ Base16 is useful

Base24/ Base16 can be used to easily generate your favourite theme for your
favourite application. Many of the template repositories provide theme files
that you can copy/ import into said application.



## Documentation

- [Styling Guidelines](styling.md)
- [Builder Guidelines](builder.md)
- [File Guidelines](file.md)
- [Roadmap/ TODO](roadmap.md)

## Template Repositories

To add your own template, submit a pull request to URL and add your repository to the list below. **Repository naming scheme: base24-\[template-name\]** (with dashes as separators).

- [CSS etc](https://github.com/Base24/base24-css-etc)  maintained by [Base24](https://github.com/Base24)
- [Gnome Terminal](https://github.com/Base24/base24-gnome-terminal)  maintained by [Base24](https://github.com/Base24)
- [HTML](https://github.com/Base24/base24-html)  maintained by [Base24](https://github.com/Base24)
- [iTerm2](https://github.com/Base24/base24-iterm2)  maintained by [Base24](https://github.com/Base24)
- [KDEPlasma](https://github.com/Base24/base24-kdeplasma)  maintained by [Base24](https://github.com/Base24)
- [Konsole](https://github.com/Base24/base24-konsole)  maintained by [Base24](https://github.com/Base24)
- [Slack](https://github.com/Base24/base24-slack)  maintained by [Base24](https://github.com/Base24)
- [Termux](https://github.com/Base24/base24-termux)  maintained by [Base24](https://github.com/Base24)
- [VSCode](https://github.com/Base24/base24-vscode)  maintained by [Base24](https://github.com/Base24)
- [Windows Terminal](https://github.com/Base24/base24-windows-terminal)  maintained by [Base24](https://github.com/Base24)
- [XFCE4 Terminal](https://github.com/Base24/base24-xfce4-terminal)  maintained by [Base24](https://github.com/Base24)



### Existing Base16 Templates
- [Alacritty](https://github.com/aaron-williamson/base16-alacritty) maintained by [aaron-williamson](https://github.com/aaron-williamson)
- [Binary Ninja](https://github.com/evanrichter/base16-binary-ninja) maintained by [evanrichter](https://github.com/evanrichter)
- [Blink](https://github.com/niklaas/base16-blink) maintained by [niklaas](https://github.com/niklaas)
- [C Header](https://github.com/m1sports20/base16-c_header) maintained by [m1sports20](https://github.com/m1sports20)
- [ConCfg](https://github.com/h404bi/base16-concfg) maintained by [h404bi](https://github.com/h404bi)
- [ConEmu](https://github.com/martinlindhe/base16-conemu) maintained by [martinlindhe](https://github.com/martinlindhe)
- [Console2](https://github.com/AFulgens/base16-console2) maintained by [AFulgens](https://github.com/AFulgens)
- [ConsoleZ](https://github.com/AFulgens/base16-consolez) maintained by [AFulgens](https://github.com/AFulgens)
- [Crosh](https://github.com/philj56/base16-crosh) maintained by [philj56](https://github.com/philj56)
- [Dunst](https://github.com/khamer/base16-dunst) maintained by [khamer](https://github.com/khamer)
- [Emacs](https://github.com/belak/base16-emacs) maintained by [belak](https://github.com/belak)
- [fzf](https://github.com/nicodebo/base16-fzf) maintained by [nicodebo](https://github.com/nicodebo)
- [Godot](https://github.com/Calinou/base16-godot) maintained by [Calinou](https://github.com/Calinou)
- [GTK+2](https://github.com/dawikur/base16-gtk2) maintained by [dawikur](https://github.com/dawikur)
- [Highlight](https://github.com/bezhermoso/base16-highlight) maintained by [bezhermoso](https://github.com/bezhermoso)
- [i3](https://github.com/khamer/base16-i3) maintained by [khamer](https://github.com/khamer)
- [i3status](https://github.com/Eluminae/base16-i3status) maintained by [Eluminae](https://github.com/Eluminae)
- [i3status-rust](https://github.com/mystfox/base16-i3status-rust) maintained by [mystfox](https://github.com/mystfox)
- [Jetbrains](https://github.com/adilosa/base16-jetbrains) maintained by [adilosa](https://github.com/adilosa)
- [JOE](https://github.com/jjjordan/base16-joe) maintained by [jjjordan](https://github.com/jjjordan)
- [Kakoune](https://github.com/leira/base16-kakoune) maintained by [leira](https://github.com/leira)
- [kitty](https://github.com/kdrag0n/base16-kitty) maintained by [kdrag0n](https://github.com/kdrag0n)
- [mako](https://github.com/Eluminae/base16-mako) maintained by [Eluminae](https://github.com/Eluminae)
- [MinTTY](https://github.com/geoffstokes/base16-mintty) maintained by [geoffstokes](https://github.com/geoffstokes)
- [MonoDevelop](https://github.com/netpyoung/base16-monodevelop) maintained by [netpyoung](https://github.com/netpyoung)
- [Prism](https://github.com/atelierbram/base16-prism) maintained by [atelierbram](https://github.com/atelierbram)
- [prompt-toolkit & ipython](https://github.com/memeplex/base16-prompt-toolkit) maintained by [memeplex](https://github.com/memeplex)
- [PuTTY](https://github.com/benjojo/base-16-putty) maintained by [benjojo](https://github.com/benjojo)
- [Pygments](https://github.com/mohd-akram/base16-pygments) maintained by [mohd-akram](https://github.com/mohd-akram)
- [QOwnNotes](https://github.com/themix-project/base16-template-qOwnNotes) maintained by [themix-project](https://github.com/themix-project)
- [Qt Creator](https://github.com/ilpianista/base16-qtcreator) maintained by [ilpianista](https://github.com/ilpianista)
- [qutebrowser](https://github.com/theova/base16-qutebrowser) maintaned by [theova](https://github.com/theova)
- [Rofi](https://gitlab.com/0xdec/base16-rofi) maintained by [0xdec](https://gitlab.com/0xdec)
- [Scide](https://github.com/brunoro/base16-scide) maintained by [brunoro](https://github.com/brunoro)
- [Shell](https://github.com/chriskempson/base16-shell) maintained by [chriskempson](https://github.com/chriskempson)
- [st](https://github.com/honza/base16-st) maintained by [honza](https://github.com/honza)
- [StumpWM](https://github.com/tpine/base16-stumpwm) maintained by [tpine](https://github.com/tpine)
- [Sway](https://github.com/rkubosz/base16-sway) maintained by [rkubosz](https://github.com/rkubosz)
- [Termite](https://github.com/khamer/base16-termite) maintained by [khamer](https://github.com/khamer)
- [TextMate & Sublime Text](https://github.com/chriskempson/base16-textmate) maintained by [chriskempson](https://github.com/chriskempson)
- [Tilix](https://github.com/karlding/base16-tilix) maintained by [karlding](https://github.com/karlding)
- [Vim](https://github.com/chriskempson/base16-vim) maintained by [chriskempson](https://github.com/chriskempson)
- [Vis](https://github.com/pshevtsov/base16-vis) maintained by [pshevtsov](https://github.com/pshevtsov)
- [Waybar](https://github.com/mnussbaum/base16-waybar) maintained by [mnussbaum](https://github.com/mnussbaum)
- [Windows Command Prompt](https://github.com/iamthad/base16-windows-command-prompt) maintained by [iamthad](https://github.com/iamthad)
- [Xcode](https://github.com/kreeger/base16-xcode) maintained by [kreeger](https://github.com/kreeger)
- [Xresources](https://github.com/binaryplease/base16-xresources) maintained by [binaryplease](https://github.com/binaryplease)
- [Xshell](https://github.com/h404bi/base16-xshell) maintained by [h404bi](https://github.com/h404bi)
- [zathura](https://github.com/nicodebo/base16-zathura) maintained by [nicodebo](https://github.com/nicodebo)

## Scheme Repositories

To add your own scheme, submit a pull request to URL and add your repository to the list below. **Repository naming scheme: base24-\[scheme-name\]-scheme** (with dashes as separators).

- [Brogrammer](https://github.com/Base24/base24-brogrammer-scheme) maintained by [Base24](https://github.com/Base24)
- [Dracula24](https://github.com/Base24/base24-dracula-scheme) maintained by [Base24](https://github.com/Base24)
- [Espresso](https://github.com/Base24/base24-espresso-scheme) maintained by [Base24](https://github.com/Base24)
- [Framer](https://github.com/Base24/base24-framer-scheme) maintained by [Base24](https://github.com/Base24)
- [Github](https://github.com/Base24/base24-github-scheme) maintained by [Base24](https://github.com/Base24)
- [One Black](https://github.com/Base24/base24-one-black-scheme) maintained by [Base24](https://github.com/Base24)
- [One Dark](https://github.com/Base24/base24-one-dark-scheme) maintained by [Base24](https://github.com/Base24)
- [One Light](https://github.com/Base24/base24-one-light-scheme) maintained by [Base24](https://github.com/Base24)

### Generated from existing themes
- [Generated from Iterm2 themes](https://github.com/Base24/base24-mbadolato-iterm2-color-schemes) maintained by [Base24](https://github.com/Base24)

### Existing Base16 Schemes
- [Atelier](https://github.com/atelierbram/base16-atelier-schemes) maintained by [atelierbram](https://github.com/atelierbram)
- [Atlas](https://github.com/ajlende/base16-atlas-scheme) maintained by [ajlende](https://github.com/ajlende)
- [Black Metal](https://github.com/metalelf0/base16-black-metal-scheme) maintained by [metalelf0](https://github.com/metalelf0)
- [Brush Trees](https://github.com/whiteabelincoln/base16-brushtrees-scheme) maintained by [whiteabelincoln](https://github.com/whiteabelincoln)
- [Circus](https://github.com/stepchowfun/base16-circus-scheme) maintained by [stepchowfun](https://github.com/stepchowfun) and [ewang12](https://github.com/ewang12)
- [Classic](https://github.com/detly/base16-classic-scheme) maintained by [detly](https://github.com/detly)
- [Codeschool](https://github.com/blockloop/base16-codeschool-scheme) maintained by [blockloop](https://github.com/blockloop)
- [Cupertino](https://github.com/Defman21/base16-cupertino) maintained by [Defman21](https://github.com/Defman21)
- [Default](https://github.com/chriskempson/base16-default-scheme) maintained by [chriskempson](https://github.com/chriskempson)
- [Fruit Soda](https://github.com/jozip/base16-fruit-soda-scheme) maintained by [jozip](https://github.com/jozip)
- [Gruvbox](https://github.com/dawikur/base16-gruvbox-scheme) maintained by [dawikur](https://github.com/dawikur)
- [Hardcore](https://github.com/callerc1/base16-hardcore-scheme) maintained by [callerc1](https://github.com/callerc1)
- [Helios](https://github.com/reyemxela/base16-helios-scheme) maintained by [reyemxela](https://github.com/reyemxela)
- [Heetch](https://github.com/tealeg/base16-heetch-scheme) maintained by [tealeg](https://github.com/tealeg)
- [Horizon](https://github.com/michael-ball/base16-horizon-scheme) maintained by [michael-ball](https://github.com/michael-ball)
- [iA](https://github.com/aramisgithub/base16-ia-scheme) maintained by [aramisgithub](https://github.com/aramisgithub)
- [Icy](https://github.com/icyphox/base16-icy-scheme) maintained by [icyphox](https://github.com/icyphox)
- [Materia](https://github.com/Defman21/base16-materia) maintained by [Defman21](https://github.com/Defman21)
- [Material Theme](https://github.com/ntpeters/base16-materialtheme-scheme) maintained by [ntpeters](https://github.com/ntpeters)
- [Material Vivid](https://github.com/joshyrobot/base16-material-vivid-scheme) maintained by [joshyrobot](https://github.com/joshyrobot)
- [Mellow](https://github.com/gidsi/base16-mellow-scheme) maintained by [gidsi](https://github.com/gidsi)
- [Mexico-Light](https://github.com/drzel/base16-mexico-light-scheme) maintained by [drzel](https://github.com/drzel)
- [Nord](https://github.com/8-uh/base16-nord-scheme) maintained by [8-uh](https://github.com/8-uh)
- [Nova](https://github.com/gessig/base16-nova-scheme) maintained by [gessig](https://github.com/gessig)
- [Outrun](https://github.com/hugodelahousse/base16-outrun-schemes) maintained by [hugodelahousse](https://github.com/hugodelahousse)
- [PaperColor](https://github.com/jonleopard/base16-papercolor-scheme) maintained by [jonleopard](https://github.com/jonleopard)
- [Porple](https://github.com/AuditeMarlow/base16-porple-scheme) maintained by [AuditeMarlow](https://github.com/AuditeMarlow)
- [Purpledream](https://github.com/archmalet/base16-purpledream-scheme) maintained by [archmalet](https://github.com/archmalet)
- [Rebecca](https://github.com/vic/base16-rebecca) maintained by [vic](https://github.com/vic)
- [Sandcastle](https://github.com/gessig/base16-sandcastle-scheme) maintained by [gessig](https://github.com/gessig)
- [Snazzy](https://github.com/h404bi/base16-snazzy-scheme) maintained by [h404bi](https://github.com/h404bi)
- [Solarflare](https://github.com/mnussbaum/base16-solarflare-scheme) maintained by [mnussbaum](https://github.com/mnussbaum)
- [Solarized](https://github.com/aramisgithub/base16-solarized-scheme) maintained by [aramisgithub](https://github.com/aramisgithub)
- [Summercamp](https://github.com/zoefiri/base16-summercamp) maintained by [zoe firi](https://github.com/zoefiri)
- [Summerfruit](https://github.com/cscorley/base16-summerfruit-scheme) maintained by [cscorley](https://github.com/cscorley)
- [Synth Midnight](https://github.com/michael-ball/base16-synth-midnight-scheme) maintained by [michael-ball](https://github.com/michael-ball)
- [Tomorrow](https://github.com/chriskempson/base16-tomorrow-scheme) maintained by [chriskempson](https://github.com/chriskempson)
- [Twilight](https://github.com/hartbit/base16-twilight-scheme) maintained by [hartbit](https://github.com/hartbit)
- [Unikitty](https://github.com/joshwlewis/base16-unikitty) maintained by [joshwlewis](https://github.com/joshwlewis)
- [Woodland](https://github.com/jcornwall/base16-woodland-scheme) maintained by [jcornwall](https://github.com/jcornwall)
- [Zenburn](https://github.com/elnawe/base16-zenburn-scheme) maintained by [elnawe](https://github.com/elnawe)
- [XCode Dust](https://github.com/gonsie/base16-xcode-dusk-scheme) maintained by [gonsie](https://github.com/gonsie)
- [Old Unclaimed Schemes](https://github.com/chriskempson/base16-unclaimed-schemes) - If your scheme is in this repository, please give it a new home!

## Builder Repositories

**Repository naming scheme: base24-builder-\[language\]** (with dashes as separators). The separate headings are the latest versions of the spec supported by each builder.

### Base24 0.1.0 (Feb 2020)

#### Changes

base00 through base0F are identical to base16. See the table below for the
Base24 fall-backs:

|Base24|Base16|
|------|------|
|base10|base00|
|base11|base00|
|base12|base08|
|base13|base0A|
|base14|base0B|
|base15|base0C|
|base16|base0D|
|base17|base0E|

#### Builders

- [Base 24 Builder Python](https://github.com/Base24/base24-builder-python) maintained by [Base24](https://github.com/Base24)

### Base16 0.9.1 (Jun 15, 2019)

#### Changes

- Make baseXX-hex-bgr variables available to templates
- Warn when a template file has been overwritten

#### Builders

- [Base 16 Builder Go](https://github.com/belak/base16-builder-go) maintained by [belak](https://github.com/belak)
- [Base 16 Builder PHP](https://github.com/chriskempson/base16-builder-php) maintained by [chriskempson](https://github.com/chriskempson)
- [Base 16 Builder Python](https://github.com/InspectorMustache/base16-builder-python) maintained by [InspectorMustache](https://github.com/InspectorMustache)
- [Base 16 Builder Rust](https://github.com/ilpianista/base16-builder-rust) maintained by [ilpianista](https://github.com/ilpianista)


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/Base24/Base24
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


## Community Files
### Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/Base24/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/Base24/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/Base24/.github/blob/master/SECURITY.md) for more information.
