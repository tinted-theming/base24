# The Evolution of Base24

The Base16 and Base24 specifications have been reevaluated to address certain shortcomings and enhance overall compatibility and usability.

## Advantages of the Proposed Changes

These adjustments introduce two additional colours and enhance support for an existing colour, offering greater flexibility and consistency within the scheme.

### Shortcomings of Base24 0.1.0

- Lack of a bright variant for the colour Brown, which was presumed deprecated.
- Colours are not arranged in 'ansi order,' complicating the mapping process to ANSI counterparts.

## Objectives of the Proposed Changes

- Transition away from the baseXX naming convention, which can be confusing for scheme and template designers, in favour of a more intuitive naming system.

## Disadvantages and Compatibility Considerations

These changes will break forwards compatibility; existing Base16 schemes will no longer function, and previous versions of Base24 schemes will become incompatible. However, backwards compatibility can be preserved with some effort, although this may require additional work from builders.

## File Structure

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

## Builder Guidelines

### Requirements
Builders should iterate through a series of local templates and schemes to generate outputs. An example file structure for input and output:

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

### Optional but Desirable
Builders may use a config file pointing to a list of schemes and fetch these through git.

Ensure backward compatibility with Base24 0.1.0 and Base16 0.9.1.

## Styling

### Example - One Dark Theme

|Name|Colour|HEX Code|RGB|
|---|---|---|---|
|bg_darkest|![bg_darkest](https://placehold.it/25/21252b/000000?text=+)|21252b|33,37,43|
|bg_dark|![bg_dark](https://placehold.it/25/282c34/000000?text=+)|282c34|40,44,52|
|black|![black](https://placehold.it/25/3f4451/000000?text=+)|3f4451|63,68,81|
|black_b|![black_b](https://placehold.it/25/4f5666/000000?text=+)|4f5666|79,86,102|
|white|![white](https://placehold.it/25/e6e6e6/000000?text=+)|e6e6e6|230,230,230|
|white_b|![white_b](https://placehold.it/25/ffffff/000000?text=+)|ffffff|255,255,255|
|red|![red](https://placehold.it/25/e06c75/000000?text=+)|e06c75|224,108,117|
|red_b|![red_b](https://placehold.it/25/ff7b86/000000?text=+)|ff7b86|255,123,134|
|green|![green](https://placehold.it/25/98c379/000000?text=+)|98c379|152,195,121|
|green_b|![green_b](https://placehold.it/25/b1e18b/000000?text=+)|b1e18b|177,225,139|
|yellow|![yellow](https://placehold.it/25/d19a66/000000?text=+)|d19a66|209,154,102|
|yellow_b|![yellow_b](https://placehold.it/25/efb074/000000?text=+)|efb074|239,176,116|
|blue|![blue](https://placehold.it/25/61afef/000000?text=+)|61afef|97,175,239|
|blue_b|![blue_b](https://placehold.it/25/67cdff/000000?text=+)|67cdff|103,205,255|
|magenta|![magenta](https://placehold.it/25/c678dd/000000?text=+)|c678dd|198,120,221|
|magenta_b|![magenta_b](https://placehold.it/25/e48bff/000000?text=+)|e48bff|228,139,255|
|cyan|![cyan](https://placehold.it/25/56b6c2/000000?text=+)|56b6c2|86,182,194|
|cyan_b|![cyan_b](https://placehold.it/25/63d4e0/000000?text=+)|63d4e0|99,212,224|

### New colours

|Name|Colour|HEX Code|RGB|
|---|---|---|---|
|orange|![orange](https://placehold.it/25/d78460/000000?text=+)|d78460|215,132,96|
|orange_b|![orange_b](https://placehold.it/25/de9a7c/000000?text=+)|de9a7c|222,154,124|
|brown|![brown](https://placehold.it/25/994949/000000?text=+)|994949|153,73,73|
|brown_b|![brown_b](https://placehold.it/25/bf5c5c/000000?text=+)|bf5c5c|191,92,92|
|pink|![pink](https://placehold.it/25/e9969d/000000?text=+)|e9969d|233,150,157|
|pink_b|![pink_b](https://placehold.it/25/eeafb4/000000?text=+)|eeafb4|238,175,180|

### Colour Mapping

The proposed mappings between Base24, the previous Base24 version, and Base16:

|Base24|Base24 (old)|Base16|
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
