import typing
import discord
from discord.ext import commands
import json
import logging
logger: logging.Logger = logging.getLogger('bot')

class Hydrate(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__()
        self.bot: discord.Bot = bot

    @discord.slash_command(name="water", description="Stay Hydrated!")  # type: ignore
    async def errorCode(self, ctx: discord) -> None:
        # do the stuff
        await ctx.respond("https://media.discordapp.net/attachments/838143799020093450/1294810328303140906/mumu_hydrate.png?ex=670c5d96&is=670b0c16&hm=de9407937154da8c76fa09ec3b8cc2d542efcfd67b804c7b74c7550c8dcb85f9&=&format=webp&quality=lossless&width=360&height=360")

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
    bot.add_cog(Hydrate(bot))
   
