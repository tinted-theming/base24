# Colours

base00 through base0F are identical to base16. See the table below for the
Base24 fallbacks:

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

- Colours base00 to base07 are typically variations of a shade and run from dark
to lightest. These colours are used for foreground and background, status bars,
line highlighting and such.

- Colours base08 to base0E are typically individual colours used for types,
operators, names and variables.

- Base0F should not be used.

- Colours base10 and base11 are an extension of base00 and span darker to darkest

- Colours base12 through base17 are brighter variants of base08 to base09 and
base0B to base0E

- In order to create a dark theme, colours base00 to base07 should span from
dark to light and colours base10 to base11 should span light (though darker
than base00) to darker still.

- For a light theme, colours base00 to base07 should span from light to dark and
colours base10 to base11 should span dark (though lighter than base00) to
lighter still.

|One Dark|baseNN|Ansi|Terminal|Text Editor|
|---|---|---|---|---|
|![#](https://place-hold.it/80x20/282c34?text=+)|base00|-|Background|Default Background|
|![#](https://place-hold.it/80x20/3f4451?text=+)|base01|0|Black|Lighter Background(Used for status bars)|
|![#](https://place-hold.it/80x20/4f5666?text=+)|base02|8|Bright Black|Selection Background|
|![#](https://place-hold.it/80x20/545862?text=+)|base03|-|NA|Comments, Invisibles, Line Highlighting|
|![#](https://place-hold.it/80x20/9196a1?text=+)|base04|-|NA|Dark Foreground (Used for status bars)|
|![#](https://place-hold.it/80x20/abb2bf?text=+)|base05|-|Foreground|Default Foreground, Caret, Delimiters, Operators|
|![#](https://place-hold.it/80x20/e6e6e6?text=+)|base06|7|White|Light Foreground (Not often used)|
|![#](https://place-hold.it/80x20/ffffff?text=+)|base07|15|Bright White|The Lightest Foreground (Not often used)|
|![#](https://place-hold.it/80x20/e06c75?text=+)|base08|1|Red|Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted|
|![#](https://place-hold.it/80x20/d19a66?text=+)|base09|3|Yellow|Integers, Boolean, Constants, XML Attributes, Markup Link Url|
|![#](https://place-hold.it/80x20/e5c07b?text=+)|base0A|~11|NA|Classes, Markup Bold, Search Text Background|
|![#](https://place-hold.it/80x20/98c379?text=+)|base0B|2|Green|Strings, Inherited Class, Markup Code, Diff Inserted|
|![#](https://place-hold.it/80x20/56b6c2?text=+)|base0C|6|Cyan|Support, Regular Expressions, Escape Characters, Markup Quotes|
|![#](https://place-hold.it/80x20/61afef?text=+)|base0D|4|Blue|Functions, Methods, Attribute IDs, Headings|
|![#](https://place-hold.it/80x20/c678dd?text=+)|base0E|5|Purple|Keywords, Storage, Selector, Markup Italic, Diff Changed|
|![#](https://place-hold.it/80x20/be5046?text=+)|base0F|-|NA|Deprecated|
|![#](https://place-hold.it/80x20/21252b?text=+)|base10|-|NA|Darker Background|
|![#](https://place-hold.it/80x20/181a1f?text=+)|base11|-|NA|The Darkest Background|
|![#](https://place-hold.it/80x20/ff7b86?text=+)|base12|9|Bright Red|NA|
|![#](https://place-hold.it/80x20/efb074?text=+)|base13|11|Bright Yellow|NA|
|![#](https://place-hold.it/80x20/b1e18b?text=+)|base14|10|Bright Green|NA|
|![#](https://place-hold.it/80x20/63d4e0?text=+)|base15|14|Bright Cyan|NA|
|![#](https://place-hold.it/80x20/67cdff?text=+)|base16|12|Bright Blue|NA|
|![#](https://place-hold.it/80x20/e48bff?text=+)|base17|13|Bright Purple|NA|
