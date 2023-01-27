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

$${\definecolor{bg_darkest}{RGB}{33,37,43}}$$
$${\definecolor{bg_dark}{RGB}{40,44,52}}$$
$${\definecolor{black}{RGB}{63,68,81}}$$
$${\definecolor{black_b}{RGB}{79,86,102}}$$
$${\definecolor{white}{RGB}{230,230,230}}$$
$${\definecolor{white_b}{RGB}{255,255,255}}$$
$${\definecolor{red}{RGB}{224,108,117}}$$
$${\definecolor{red_b}{RGB}{255,123,134}}$$
$${\definecolor{green}{RGB}{152,195,121}}$$
$${\definecolor{green_b}{RGB}{177,225,139}}$$
$${\definecolor{yellow}{RGB}{209,154,102}}$$
$${\definecolor{yellow_b}{RGB}{239,176,116}}$$
$${\definecolor{blue}{RGB}{97,175,239}}$$
$${\definecolor{blue_b}{RGB}{103,205,255}}$$
$${\definecolor{magenta}{RGB}{198,120,221}}$$
$${\definecolor{magenta_b}{RGB}{228,139,255}}$$
$${\definecolor{cyan}{RGB}{86,182,194}}$$
$${\definecolor{cyan_b}{RGB}{99,212,224}}$$
$${\definecolor{orange}{RGB}{215,132,96}}$$
$${\definecolor{orange_b}{RGB}{222,154,124}}$$
$${\definecolor{brown}{RGB}{153,73,73}}$$
$${\definecolor{brown_b}{RGB}{191,92,92}}$$
$${\definecolor{pink}{RGB}{233,150,157}}$$
$${\definecolor{pink_b}{RGB}{238,175,180}}$$

## One Dark

|Name|Colour|HEX Code|RGB|
|---|---|---|---|
|bg_darkest|$${\colorbox{bg_darkest}{...}}$$|21252b|33,37,43|
|bg_dark|$${\colorbox{bg_dark}{...}}$$|282c34|40,44,52|
|black|$${\colorbox{black}{...}}$$|3f4451|63,68,81|
|black_b|$${\colorbox{black_b}{...}}$$|4f5666|79,86,102|
|white|$${\colorbox{white}{...}}$$|e6e6e6|230,230,230|
|white_b|$${\colorbox{white_b}{...}}$$|ffffff|255,255,255|
|red|$${\colorbox{red}{...}}$$|e06c75|224,108,117|
|red_b|$${\colorbox{red_b}{...}}$$|ff7b86|255,123,134|
|green|$${\colorbox{green}{...}}$$|98c379|152,195,121|
|green_b|$${\colorbox{green_b}{...}}$$|b1e18b|177,225,139|
|yellow|$${\colorbox{yellow}{...}}$$|d19a66|209,154,102|
|yellow_b|$${\colorbox{yellow_b}{...}}$$|efb074|239,176,116|
|blue|$${\colorbox{blue}{...}}$$|61afef|97,175,239|
|blue_b|$${\colorbox{blue_b}{...}}$$|67cdff|103,205,255|
|magenta|$${\colorbox{magenta}{...}}$$|c678dd|198,120,221|
|magenta_b|$${\colorbox{magenta_b}{...}}$$|e48bff|228,139,255|
|cyan|$${\colorbox{cyan}{...}}$$|56b6c2|86,182,194|
|cyan_b|$${\colorbox{cyan_b}{...}}$$|63d4e0|99,212,224|

### New (and optional)

|Name|Colour|HEX Code|RGB|
|---|---|---|---|
|orange|$${\colorbox{orange}{...}}$$|d78460|215,132,96|
|orange_b|$${\colorbox{orange_b}{...}}$$|de9a7c|222,154,124|
|brown|$${\colorbox{brown}{...}}$$|994949|153,73,73|
|brown_b|$${\colorbox{brown_b}{...}}$$|bf5c5c|191,92,92|
|pink|$${\colorbox{pink}{...}}$$|e9969d|233,150,157|
|pink_b|$${\colorbox{pink_b}{...}}$$|eeafb4|238,175,180|

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
