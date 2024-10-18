import discord
from discord.ext import commands
import logging
from lib.types.card import Card
from lib.types import element as element_type
from lib.types.errors import ElementDoesNotExist
logger: logging.Logger = logging.getLogger('bot')

class CardCog(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__()
        self.bot: discord.Bot = bot

    @discord.slash_command(name="card", description="get a dummy card (default is hydro)")  # type: ignore
    async def errorCode(self, ctx: discord.commands.ApplicationContext, element: str = "hydro") -> None:
        c = Card("Furina", element_type.get_by_name(element), cost=len(element))
        await ctx.respond(embed=c.create_embed())  # type: ignore

    @errorCode.error  # type: ignore
    async def errorCodeErr(self, ctx: discord.commands.ApplicationContext, error: discord.ApplicationCommandError) -> None:
        if isinstance(error.__cause__.__class__, ElementDoesNotExist):
            await ctx.respond( # type: ignore
                "Element does not exist",
                ephemeral=True
            ) # type: ignore
        else:
            logger.error(error, stack_info=True)
            await ctx.respond("ERROR yay", ephemeral=True)  # type: ignore


def setup(bot: discord.Bot) -> None:
    bot.add_cog(CardCog(bot))
