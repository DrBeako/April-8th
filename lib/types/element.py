import json
from lib.types.errors import *

class Element:
	def __init__(self, name: str, colour: str) -> None:
		assert name, colour
		self.name: str = name
		self.colour: str = colour

def get_by_name(name: str) -> Element:
	json_data = json.load(open("./data/elements.json", encoding="utf-8"))
	try:
		element_data = json_data.get(name)
		return Element(
			name=element_data.get("name"),
			colour=element_data.get("colour", "#ff0000")
		)
	except:
		raise ElementDoesNotExist