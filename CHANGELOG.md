# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).


### Base24 0.1.0 (Feb 2020)

#### Changes

base00 through base0F are identical to base16. See the table below for the
Base24 fall-backs:

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

#### Builders

- [Base24 Builder Python](https://github.com/Base24/base24-builder-python)

### Base16 0.9.1 (Jun 15, 2019)

#### Changes

- Make baseXX-hex-bgr variables available to templates
- Warn when a template file has been overwritten

#### Builders

- [Base16 Builder Go](https://github.com/belak/base16-builder-go)
- [Base16 Builder PHP](https://github.com/chriskempson/base16-builder-php)
- [Base16 Builder Python](https://github.com/InspectorMustache/base16-builder-python)
- [Base16 Builder Rust](https://github.com/ilpianista/base16-builder-rust)
