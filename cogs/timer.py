import typing
import discord
from discord.ext import commands
import json
import logging
import time
logger: logging.Logger = logging.getLogger('bot')

class Timer(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__()
        self.bot: discord.Bot = bot

    @discord.slash_command(name="timer", description="A progress bar will be summoned to time for you")  # type: ignore
    async def errorCode(self, ctx: discord.Message, timer: int, unit: str | None = None) -> None:
        # do the stuff
        # verify to run or not, if 0 then it woudn't run
        verify = 1
        # total amount of bar emote able to shown
        emotelength = 2
        # default unit
        unit = "s"
        if unit == "min":
            timer = 60 * timer
        elif unit == "hr":
            timer = 3600 * timer
        elif unit =="s":
            timer = timer
        else:
            await ctx.respond("This unit is not supported! Please input only hr (hours) min (minutes) or s (seconds)!")
            verify = 0
        sleeptime = timer / emotelength

        if sleeptime < 0.5:
            await ctx.respond ("Discord hates it if I send 2 messages every second1! Please set a minimum of 1 seconds!")
            verify = 0
        
        if verify == 1:
            await ctx.respond("Timer of " + str(timer) + str(unit) + " have been set!")
            for i in range(emotelength):
                time.sleep (sleeptime)
                await ctx.respond (":clock1:")
            await ctx.respond("Ring ring ring")  # type: ignore

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
    bot.add_cog(Timer(bot))
