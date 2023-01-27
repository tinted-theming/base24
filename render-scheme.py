

import sys
from pathlib import Path
import yaml

def hexToRGB(hex:str):
	return f"{int(hex[0:2], 16)},{int(hex[2:4], 16)},{int(hex[4:6], 16)}"

if __name__ == "__main__":
	if len(sys.argv) < 2:
		sys.exit
	exampleFile = Path(sys.argv[1])
	if not exampleFile.exists():
		sys.exit(1)

	example = yaml.safe_load(exampleFile.read_text('utf-8'))

	name = example.pop("name")
	example.pop("author")

	for base, value in example.items():
		print(f"$$\u007b\\definecolor\u007b{base}\u007d\u007bRGB\u007d\u007b{hexToRGB(value)}\u007d\u007d$$")

	print(f"""

## {name}

|Name|Colour|HEX Code|RGB|
|---|---|---|---|""")

	for base, value in example.items():
		print(f"|{base}|$$\u007b\\colorbox\u007b{base}\u007d\u007b{...}\u007d\u007d$$|{value}|{hexToRGB(value)}|")
