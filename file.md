# File Guidelines
Base24 specifies the format of two types of files: scheme files, used for
defining the colours that are to be assigned to a template when processed
by a Builder, and config files, used by templates to pass information to a
Builder when using a template.

## Template Config Files
Template files reside in a `templates` folder and have the name
`config.yaml`. These files have the following example structure:

```yaml
default:
	extension: .file-extension
	output: output-directory-name

additional:
	extension: .file-extension
	output: output-directory-name
```

This example specifies that a Builder is to parse two template files:
`templates/default.mustache` and `templates/additional.mustache`. `extension`
defines the extension of the file that will be produced by a Builder, e.g.
`base24-default-dark.file-extension`, and `output` defines the output directory
that will be created within the templates root directory where the processed
templates will be created, e.g.
`output-directory-name/base24-default-dark.file-extension`.

## Scheme Files
Scheme files have the following example structure:

```yaml
scheme: "Scheme Name"
author: "Scheme Author"
base00: "282c34"
base01: "3f4451"
base02: "4f5666"
base03: "545862"
base04: "9196a1"
base05: "abb2bf"
base06: "e6e6e6"
base07: "ffffff"
base08: "e06c75"
base09: "d19a66"
base0A: "e5c07b"
base0B: "98c379"
base0C: "56b6c2"
base0D: "61afef"
base0E: "c678dd"
base0F: "be5046"
base10: "21252b"
base11: "181a1f"
base12: "ff7b86"
base13: "efb074"
base14: "b1e18b"
base15: "63d4e0"
base16: "67cdff"
base17: "e48bff"
```

Hexadecimal colour values should not be preceded by a "#".
