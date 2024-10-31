import typing
import discord
from discord.ext import commands
import json
import logging
import random
from lib.types.roll import DicePhase
from lib.types.roll import convert_id
logger: logging.Logger = logging.getLogger('bot')

class MultiDiceRoll(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__()
        self.bot: discord.Bot = bot

    @discord.slash_command(name="roll_more", description="roll multiple dice")  # type: ignore
    async def errorCode(self, ctx: discord, amount: int) -> None:
        # do the stuff
        rolltime = 0
        total = "none"
        while rolltime < amount:
            result = random.randint(1,8)
            word = convert_id(result)
            rolltime = rolltime + 1
            if total == "none":
                total = word
            total = word + total

        await ctx.respond(f"{total}")


    @errorCode.error  # type: ignore
    async def errorCodeErr(self, ctx: discord.Message, error: discord.ApplicationCommandError) -> None:
        if isinstance(error.__cause__.__class__, (KeyError)):
            await ctx.respond(
                ephemeral=True
            )
        else:
            logger.error("errorCode", exc_info=error, stack_info=True)
            await ctx.respond("ERROR yay", ephemeral=True)  # type: ignore
def setup(bot: discord.Bot) -> None:
    bot.add_cog(MultiDiceRoll(bot))