import typing
import discord
from discord.ext import commands
import json
import logging
import random
from lib.types.roll import DicePhase
from lib.types.roll import convert_id
logger: logging.Logger = logging.getLogger('bot')

# dice counts
omni = 0
pyro = 0
cryo = 0
electro = 0
dendro = 0
hydro = 0
anemo = 0
geo = 0

class MultiDiceRoll(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__()
        self.bot: discord.Bot = bot

    @discord.slash_command(name="roll_more", description="roll multiple dice")  # type: ignore
    async def errorCode(self, ctx: discord, amount: int) -> None:
        # do the stuff
        # defining variable for loops
        total = "You didn't roll shit"
        omni = 0
        pyro = 0
        cryo = 0
        electro = 0
        dendro = 0
        hydro = 0
        anemo = 0
        geo = 0
        rolling = amount
        for i in range(rolling):
            result = random.randint(1,8)
            # counting dice
            if result == 1:
                omni = omni + 1
            elif result == 2:
                pyro = pyro + 1
            elif result == 3:
                cryo = cryo + 1
            elif result == 4:
                electro = electro + 1
            elif result == 5:
                dendro = dendro + 1
            elif result == 6:
                hydro = hydro + 1
            elif result == 7:
                anemo = anemo + 1
            elif result == 8:
                geo = geo + 1
            output = convert_id(result)
            # replacing initial total veriable with first result
            if total == "You didn't roll shit":
                total = output
            else:
                total = output + total

        await ctx.respond(f"{total}")
        await ctx.respond(f"There are {omni} omni, {pyro} pyro, {cryo} cryo, {electro} electro, {dendro} dendro, {hydro} hydro, {anemo} anemo, {geo} geo")


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