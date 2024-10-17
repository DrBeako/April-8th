import os
import discord
from dotenv import load_dotenv  # type: ignore
from lib.logsetup import init_log
import peewee
from models import *

init_log()
load_dotenv()
# intents: discord.Intents = discord.Intents.all()
# intents.members = True

bot = discord.Bot() # intents=intents


def add_exts(path: str) -> None:
    if "__pycache__" in path:
        return
    if os.path.isdir(path):
        for p in os.listdir(path):
            add_exts(f"{path}/{p}")
    elif path.endswith(".py"):
        bot.load_extension(path[2:-3].replace("/", "."))

add_exts("./cogs")

# @bot.event
# async def on_ready() -> None:
#     pass

# @bot.event
# async def on_member_remove(member: discord.Member) -> None:
#     """deletes user file in ./data/userdata/ when leaving server"""
#     User.delete_by_id(member.id)

if __name__ == '__main__':
    db = BaseModel._meta.database
    db.init(database=os.getenv("DB_PATH"), pragmas={'foreign_keys': 1})
    db.connect()
    db.create_tables([...])
    # db.close()

    bot.run(token=os.getenv("TOKEN"), reconnect=True)
