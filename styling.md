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
|![#](https://placehold.it/25/282c34/000000?text=+)|base00|-|Background|Default Background|
|![#](https://placehold.it/25/3f4451/000000?text=+)|base01|0|Black|Lighter Background(Used for status bars)|
|![#](https://placehold.it/25/4f5666/000000?text=+)|base02|8|Bright Black|Selection Background|
|![#](https://placehold.it/25/545862/000000?text=+)|base03|-|NA|Comments, Invisibles, Line Highlighting|
|![#](https://placehold.it/25/9196a1/000000?text=+)|base04|-|NA|Dark Foreground (Used for status bars)|
|![#](https://placehold.it/25/abb2bf/000000?text=+)|base05|-|Foreground|Default Foreground, Caret, Delimiters, Operators|
|![#](https://placehold.it/25/e6e6e6/000000?text=+)|base06|7|White|Light Foreground (Not often used)|
|![#](https://placehold.it/25/ffffff/000000?text=+)|base07|15|Bright White|The Lightest Foreground (Not often used)|
|![#](https://placehold.it/25/e06c75/000000?text=+)|base08|1|Red|Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted|
|![#](https://placehold.it/25/d19a66/000000?text=+)|base09|3|Yellow|Integers, Boolean, Constants, XML Attributes, Markup Link Url|
|![#](https://placehold.it/25/e5c07b/000000?text=+)|base0A|~11|NA|Classes, Markup Bold, Search Text Background|
|![#](https://placehold.it/25/98c379/000000?text=+)|base0B|2|Green|Strings, Inherited Class, Markup Code, Diff Inserted|
|![#](https://placehold.it/25/56b6c2/000000?text=+)|base0C|6|Cyan|Support, Regular Expressions, Escape Characters, Markup Quotes|
|![#](https://placehold.it/25/61afef/000000?text=+)|base0D|4|Blue|Functions, Methods, Attribute IDs, Headings|
|![#](https://placehold.it/25/c678dd/000000?text=+)|base0E|5|Purple|Keywords, Storage, Selector, Markup Italic, Diff Changed|
|![#](https://placehold.it/25/be5046/000000?text=+)|base0F|-|NA|Deprecated|
|![#](https://placehold.it/25/21252b/000000?text=+)|base10|-|NA|Darker Background|
|![#](https://placehold.it/25/181a1f/000000?text=+)|base11|-|NA|The Darkest Background|
|![#](https://placehold.it/25/ff7b86/000000?text=+)|base12|9|Bright Red|NA|
|![#](https://placehold.it/25/efb074/000000?text=+)|base13|11|Bright Yellow|NA|
|![#](https://placehold.it/25/b1e18b/000000?text=+)|base14|10|Bright Green|NA|
|![#](https://placehold.it/25/63d4e0/000000?text=+)|base15|14|Bright Cyan|NA|
|![#](https://placehold.it/25/67cdff/000000?text=+)|base16|12|Bright Blue|NA|
|![#](https://placehold.it/25/e48bff/000000?text=+)|base17|13|Bright Purple|NA|
