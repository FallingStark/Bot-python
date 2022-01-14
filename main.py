"""Discord bot with python"""

import os
import random
import logging
import sys
import pprint
import psutil
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    filename="log_bot.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s : %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

DESCRIPTION = """An example Client to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True

Client = commands.Bot(command_prefix="?", description=DESCRIPTION, intents=intents)



@Client.event
async def on_ready():
    """When client is ready"""
    logging.info(f"{Client.user.name} is ready")
    print(f"{Client.user.name} is ready")

@Client.event
async def on_connect():
    """When client is connected to discord"""
    logging.info(f"{Client.user.name} is connected to discord")
    print(f"{Client.user.name} is connected to discord")

@Client.event
async def on_disconnect():
    """When client is disconnected to discord"""
    logging.info(f"{Client.user.name} is disconnected to discord")
    print(f"{Client.user.name} is disconnected to discord")


@Client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@Client.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        await ctx.send("Format has to be in NdN!")
        return

    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@Client.command(DESCRIPTION="For when you wanna settle the score some other way")
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@Client.command()
async def repeat(ctx, times: int, content="repeating..."):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@Client.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send("{0.name} joined in {0.joined_at}".format(member))


@Client.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send("No, {0.subcommand_passed} is not cool".format(ctx))


@cool.command(name="bot")
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send("Yes, the bot is cool.")

@Client.command()
async def test(ctx):
    pprint.pprint(ctx)
    await ctx.send("Info envoyer des les logs")

@Client.command()
async def KillBot(_):
    print("le bot va dead")
    await Client.close()
    print('le bot est dead')

@Client.command()
async def restart(_):
    print("Le bot va restart")
    os.execv(sys.argv[0], sys.argv)

Client.run(os.environ.get("TOKEN"))

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception as e:
        logging.error(e)

    python = sys.executable
    os.execl(python, python, *sys.argv)