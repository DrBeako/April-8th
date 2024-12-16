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

class function_diceroll(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__()
        self.bot: discord.Bot = bot

    @discord.slash_command(name="function_roll", description="roll multiple dice but as a function")  # type: ignore
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
        result = 0
        rolled = 0
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
        await ctx.respond(f"There are {omni} omni, {pyro} pyro, {cryo} cryo, {electro} electro, {dendro} dendro, {hydro} hydro, {anemo} anemo, {geo} geo")
        rolled = rolling

        # loop to print dice sequence
        while rolled > 0:
            if omni > 0:
                if total == "You didn't roll shit":
                    total = "omni "
                    omni = omni - 1
                else:
                    total = total + "omni "
                    omni = omni - 1
            elif pyro > 0:
                if total == "You didn't roll shit":
                    total = ":fire: "
                    pyro = pyro - 1
                else:
                    total = total + ":fire: "
                    pyro = pyro - 1
            elif cryo > 0:
                if total == "You didn't roll shit":
                    total = ":ice_cube: "
                    cryo = cryo - 1
                else:
                    total = total + ":ice_cube: "
                    cryo = cryo - 1
            elif electro > 0:
                if total == "You didn't roll shit":
                    total = ":zap: "
                    electro = electro - 1
                else:
                    total = total + ":zap: "
                    electro = electro - 1
            elif dendro > 0:
                if total == "You didn't roll shit":
                    total = ":shamrock: "
                    dendro = dendro - 1
                else:
                    total = total + ":shamrock: "
                    dendro = dendro - 1
            elif hydro > 0:
                if total == "You didn't roll shit":
                    total = ":ocean: "
                    hydro = hydro - 1
                else:
                    total = total + ":ocean: "
                    hydro = hydro - 1
            elif anemo > 0:
                if total == "You didn't roll shit":
                    total = ":wind_chime: "
                    anemo = anemo - 1
                else:
                    total = total + ":wind_chime: "
                    anemo = anemo - 1
            elif geo > 0:
                if total == "You didn't roll shit":
                    total = ":rock: "
                    geo = geo - 1
                else:
                    total = total + ":rock: "
                    geo = geo - 1
            else: 
                await ctx.respond(f"{total}")
                rolled = 0


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
    bot.add_cog(function_diceroll(bot))