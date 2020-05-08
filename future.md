# The future of Base24

Parts of the Base16 and Base24 spec are not particularly widely used so this
file is a proposal on making some changes to the specification

## Advantages of these changes
These changes include two additional colours and improve support for an existing
colour.

Shortfalls of Base24 0.1.0:
Brown does not have a bright variant - this was as the colour was presumed
deprecated
Colours are not in 'ansi order' - that is the mental gymnastics to map base24
colours to the ansi counterparts are more challenging than desired

These changes aim to remediate these challenges

Move away from baseXX naming as this can be confusing for scheme and template
designers, instead support a naming system.

## Disadvantages of these changes
This will break forwards compatibility. i.e. base16 schemes will not work and
previous versions of base24 schemes will no longer work.

Backwards compatibility can be preserved, though this will lead to more work for
the builder. Most programmers should be able to implement this backwards
compatibility with minimal headache.

## File

### Schemes

```yaml
name: "Scheme Name"
author: "Scheme Author"
bg_darkest: "21252b"
bg_dark: "282c34"
black_b: "4f5666"
bg: "3f4451"
fg: "e6e6e6"
fg_lightest: "ffffff"
...
```

## Builder

### Requirements
Builders must iterate through a series of local templates and schemes to
produce some sane output. An example input/ output file structure may be:

```none
input/schemes
     /templates
output/[template_name_0]/[scheme_name_0]/data
                        /[scheme_name_1]/data
      /[template_name_1]/[scheme_name_0]/data
                        /[scheme_name_1]/data
```

Support variations of the names as listed under styling (in parentheses)

Support variations of the names supporting the following variations:
```none
HEX
	RGB
	R
	G
	B
INT
	RGB
	R
	G
	B
DEC
	RGB
	R
	G
	B
```

An example of this may be white_b_int_r

### Optional but desirable
Builders may use a config file pointing to a list of schemes and fetch these
through git.

Be backwards compatible with Base24 0.1.0 and Base16 0.9.1

## Styling

|One Dark|name|Ansi|Terminal|Text Editor|
|---|---|---|---|---|
|![#](https://placehold.it/25/21252b/000000?text=+)|bg_darkest|-|NA|The Darkest Background|
|![#](https://placehold.it/25/282c34/000000?text=+)|bg_dark|-|Background|Darker Background|
|![#](https://placehold.it/25/3f4451/000000?text=+)|bg (black)|0|Black|Default Background|
|![#](https://placehold.it/25/4f5666/000000?text=+)|black_b|8|Bright Black|Selection Background|
|![#](https://placehold.it/25/e6e6e6/000000?text=+)|fg (white)|7|White|Light Foreground|
|![#](https://placehold.it/25/ffffff/000000?text=+)|fg_lightest (white_b)|15|Bright White|The Lightest Foreground|
|![#](https://placehold.it/25/e06c75/000000?text=+)|red|1|Red|Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted|
|![#](https://placehold.it/25/ff7b86/000000?text=+)|red_b|9|Bright Red|NA|
|![#](https://placehold.it/25/98c379/000000?text=+)|green|2|Green|Strings, Inherited Class, Markup Code, Diff Inserted|
|![#](https://placehold.it/25/b1e18b/000000?text=+)|green_b|10|Bright Green|NA|
|![#](https://placehold.it/25/d19a66/000000?text=+)|yellow|3|Yellow|Integers, Boolean, Constants, XML Attributes, Markup Link Url|
|![#](https://placehold.it/25/efb074/000000?text=+)|yellow_b|11|Bright Yellow|NA|
|![#](https://placehold.it/25/61afef/000000?text=+)|blue|4|Blue|Functions, Methods, Attribute IDs, Headings|
|![#](https://placehold.it/25/67cdff/000000?text=+)|blue_bright|12|Bright Blue|NA|
|![#](https://placehold.it/25/c678dd/000000?text=+)|magenta(purple)|5|Purple|Keywords, Storage, Selector, Markup Italic, Diff Changed|
|![#](https://placehold.it/25/e48bff/000000?text=+)|magenta_b (purple_b)|13|Bright Purple|NA|
|![#](https://placehold.it/25/56b6c2/000000?text=+)|cyan|6|Cyan|Support, Regular Expressions, Escape Characters, Markup Quotes|
|![#](https://placehold.it/25/63d4e0/000000?text=+)|cyan_b|14|Bright Cyan|N/A|

### New (and optional)

|One Dark|name|Ansi|Terminal|Text Editor|
|---|---|---|---|---|
|![#](https://placehold.it/25/d78460/000000?text=+)|orange|-|N/A|N/A|
|![#](https://placehold.it/25/de9a7c/000000?text=+)|orange_b|-|N/A|N/A|
|![#](https://placehold.it/25/994949/000000?text=+)|brown|-|N/A|Opening/Closing Embedded Language Tags|
|![#](https://placehold.it/25/bf5c5c/000000?text=+)|brown_b|-|N/A|N/A|N/A|
|![#](https://placehold.it/25/e9969d/000000?text=+)|pink|-|N/A|N/A|
|![#](https://placehold.it/25/eeafb4/000000?text=+)|pink_b|-|N/A|N/A|


## Proposed mappings

|Base24|Base24(old)|Base16|
|---|---|---|
|bg_darkest|base11|base00|
|bg_dark|base10|base00|
|bg (black)|base00|base00|
|black_b|base01|base01|
|fg (white)|base06|base06|
|fg_lightest (white_b)|base07|base07|
|red|base08|base08|
|red_b|base12|base08|
|green|base0B|base0B|
|green_b|base14|base0B|
|yellow|base09|base09|
|yellow_b|base13|base0A|
|blue|base0D|base0D|
|blue_bright|base16|base0D|
|magenta(purple)|base0E|base0E|
|magenta_b (purple_b)|base17|base0E|
|cyan|base0C|base0C|
|cyan_b|base15|base0C|
