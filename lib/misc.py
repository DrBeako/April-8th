import re
from lib.types.errors import InvalidHexColorCode

def hex_to_rgb(hex_colour: str) -> tuple[int, ...]:
	if not re.match(r"#?(([0-9A-Fa-f]{6})|([0-9A-Fa-f]{3}))", hex_colour):
		raise InvalidHexColorCode
	hex_colour = hex_colour.strip('#')
	t: int = 2 if len(hex_colour) == 6 else 1
	return tuple([int(hex_colour[i*t:(i+1)*t]*(~t+4), 16) for i in range(3)]) # ~t+4 converts t to 1 or 2 if it was 2 or 1 respectively so #123 becomes #112233