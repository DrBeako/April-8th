import json
import typing
import discord
import logging
from lib.misc import hex_to_rgb
logger: logging.Logger = logging.getLogger('bot')
from . import element
from .element import Element

class Card:
	def __init__(self, char: str, element: Element, cost: int) -> None:
		self.character: str = char
		self.element: Element = element
		self.cost: int = cost
		# idk what stuff is needed we gotta see

	def create_embed(self) -> discord.Embed:
		return discord.Embed(
			colour=discord.colour.Colour.from_rgb(*hex_to_rgb(self.element.colour)),
			title=self.element.name
		)

def from_json(file: str) -> Card:
	with open(file, 'r') as f:
		json_data: dict[str, typing.Any] = json.load(f)
		element_name: str = json_data.get("element", "undefined element")
		return Card(
			json_data.get("name", "undefined name"),
			element.get_by_name(element_name),
			json_data.get("cost", "undefined cost")
		)