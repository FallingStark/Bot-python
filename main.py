"""Discord bot with python"""

from datetime import datetime
import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand

load_dotenv()

logging.basicConfig(
    filename="log_bot.log",
    filemode="w",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s : %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

DESCRIPTION = """An example Client to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True

Client = commands.Bot(command_prefix="!", description=DESCRIPTION, intents=intents)
slash = SlashCommand(Client, sync_commands=True)


@Client.command(name="tt")
async def test(ctx):
    print(Client.guilds)


@Client.command()
async def KillBot(ctx):
    await ctx.send(f"Pourquoi m'a tu tué {ctx.author.name}")
    await Client.close()


for file in os.listdir("./category"):  # lists all the cog files inside the cog folder.
    if file.endswith(".py"):  # It gets all the cogs that ends with a ".py".
        name = file[:-3]  # It gets the name of the file removing the ".py"
        Client.load_extension(f"category.{name}")  # This loads the cog.
        print(name)


Client.run(os.environ.get("TOKEN"))
