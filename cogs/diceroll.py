import typing
import discord
from discord.ext import commands
import json
import logging
logger: logging.Logger = logging.getLogger('bot')

class DiceRoll(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__()
        self.bot: discord.Bot = bot

    @discord.slash_command(name="roll", description="roll dice")  # type: ignore
    async def errorCode(self, ctx: discord) -> None:
        # do the stuff
        await ctx.respond("response", ephemeral=True)  # type: ignore

    @errorCode.error  # type: ignore
    async def errorCodeErr(self, ctx: discord.Message, error: discord.ApplicationCommandError) -> None:
        if isinstance(error.__cause__.__class__, (KeyError)):
            await ctx.respond(
                ephemeral=True
            )
        else:
            logger.error(error, stack_info=True)
            await ctx.respond("ERROR yay", ephemeral=True)  # type: ignore


def setup(bot: discord.Bot) -> None:
    bot.add_cog(DiceRoll(bot))