# Builder

Most builders can be easily adapted from the Base16 counterparts

Using https://github.com/Base24/base24-builder-python for an example

```python
# updater.py
def write_sources_file():
    """Write a sources.yaml file to current working dir."""
    file_content = (
        "schemes: "
        "https://github.com/chriskempson/base16-schemes-source.git\n"
        "templates: "
        "https://github.com/chriskempson/base16-templates-source.git"
    )
    file_path = rel_to_cwd("sources.yaml")
    with open(file_path, "w") as file_:
        file_.write(file_content)

# builder.py

def format_scheme(scheme, slug):
    """Change $scheme so it can be applied to a template."""
    scheme["scheme-name"] = scheme.pop("scheme")
    scheme["scheme-author"] = scheme.pop("author")
    scheme["scheme-slug"] = slug
    bases = ["base{:02X}".format(x) for x in range(0, 16)]
    for base in bases:
        scheme["{}-hex".format(base)] = scheme.pop(base)
        scheme["{}-hex-r".format(base)] = scheme["{}-hex".format(base)][0:2]
        scheme["{}-hex-g".format(base)] = scheme["{}-hex".format(base)][2:4]
        scheme["{}-hex-b".format(base)] = scheme["{}-hex".format(base)][4:6]
        scheme["{}-hex-bgr".format(base)] = reverse_hex(scheme["{}-hex".format(base)])

        scheme["{}-rgb-r".format(base)] = str(int(scheme["{}-hex-r".format(base)], 16))
        scheme["{}-rgb-g".format(base)] = str(int(scheme["{}-hex-g".format(base)], 16))
        scheme["{}-rgb-b".format(base)] = str(int(scheme["{}-hex-b".format(base)], 16))

        scheme["{}-dec-r".format(base)] = str(
            int(scheme["{}-rgb-r".format(base)]) / 255
        )
        scheme["{}-dec-g".format(base)] = str(
            int(scheme["{}-rgb-g".format(base)]) / 255
        )
        scheme["{}-dec-b".format(base)] = str(
            int(scheme["{}-rgb-b".format(base)]) / 255
        )
```

Was adapted to

```python
# updater.py
def write_sources_file():
	"""Write a sources.yaml file to current working dir."""
	file_content = (
		"schemes: "
		"https://github.com/Base24/base24-schemes-source.git\n"
		"templates: "
		"https://github.com/Base24/base24-templates-source.git"
	)
	file_path = rel_to_cwd("sources.yaml")
	with open(file_path, "w") as file_:
		file_.write(file_content)

#builder.py
def format_scheme(scheme, slug):
	"""Change $scheme so it can be applied to a template."""
	scheme["scheme-name"] = scheme.pop("scheme")
	scheme["scheme-author"] = scheme.pop("author")
	scheme["scheme-slug"] = slug
	bases = ["base{:02X}".format(x) for x in range(0, 16)]
	for base in bases:
		scheme["{}-hex".format(base)] = scheme.pop(base)

	extended_bases = ["base{:02X}".format(x) for x in range(16, 24)]
	base_map = {"base10": "base00", "base11": "base00", "base12": "base08", "base13": "base0A", "base14": "base0B", "base15": "base0C", "base16": "base0D", "base17": "base0E"}
	for extended_base in extended_bases:
		if extended_base in scheme:
			scheme["{}-hex".format(extended_base)] = scheme.pop(extended_base)
		else:
			scheme["{}-hex".format(extended_base)] = scheme["{}-hex".format(base_map[extended_base])]

	all_bases = ["base{:02X}".format(x) for x in range(0, 24)]
	for all_base in all_bases:
		scheme["{}-hex-r".format(all_base)] = scheme["{}-hex".format(all_base)][0:2]
		scheme["{}-hex-g".format(all_base)] = scheme["{}-hex".format(all_base)][2:4]
		scheme["{}-hex-b".format(all_base)] = scheme["{}-hex".format(all_base)][4:6]
		scheme["{}-hex-bgr".format(all_base)] = reverse_hex(scheme["{}-hex".format(all_base)])

		scheme["{}-rgb-r".format(all_base)] = str(int(scheme["{}-hex-r".format(all_base)], 16))
		scheme["{}-rgb-g".format(all_base)] = str(int(scheme["{}-hex-g".format(all_base)], 16))
		scheme["{}-rgb-b".format(all_base)] = str(int(scheme["{}-hex-b".format(all_base)], 16))

		scheme["{}-dec-r".format(all_base)] = str(
			int(scheme["{}-rgb-r".format(all_base)]) / 255
		)
		scheme["{}-dec-g".format(all_base)] = str(
			int(scheme["{}-rgb-g".format(all_base)]) / 255
		)
		scheme["{}-dec-b".format(all_base)] = str(
			int(scheme["{}-rgb-b".format(all_base)]) / 255
		)
```

For more information on base16 builders, see:

https://github.com/chriskempson/base16/blob/master/builder.md
