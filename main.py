"""Discord bot with python"""

from datetime import datetime
from math import fabs
import os
import random
import logging
from unicodedata import name
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

Client = commands.Bot(command_prefix="", description=DESCRIPTION, intents=intents)


@Client.event
async def on_ready():
    """When client is ready"""
    logging.info(f"{Client.user.name} is ready")
    print(f"{Client.user.name} is ready")
    await Client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="raphtalia")
    )


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


@Client.command(name="tt")
async def test(ctx):
    print(Client.guilds)


@Client.command()
async def KillBot(ctx):
    await ctx.send(f"Pourquoi m'a tu tué {ctx.author.name}")
    await Client.close()


@Client.command()
async def aboutme(ctx):
    def format_date(date_raw):
        date_formater = datetime.strptime(str(date_raw), "%Y-%m-%d %H:%M:%S.%f")
        date_formated = date_formater.strftime("le %d/%m/%Y à %Hh%M et %Ss")
        return date_formated

    author_created_at = format_date(ctx.author.created_at)
    author_joined_at = format_date(ctx.author.joined_at)

    role_list = ", ".join([str(r.name) for r in ctx.author.roles])

    embed = discord.Embed(
        title=f"Infos sur {ctx.author.name}",
        description=f"Voici les infos sur {ctx.author.name}",
    )
    embed.set_thumbnail(url=ctx.author.avatar_url).add_field(
        name="Dates :",
        value=f"Date de creation : {author_created_at} \n Date de join au serv : {author_joined_at}",
        inline=False,
    ).add_field(
        name="Roles sur ce serveur :",
        value=f"{role_list}",
        inline=False
    ).add_field(
        name="Id",
        value=ctx.author.id,
        inline=False
    ).add_field(
        name="Voice",
        value=ctx.author.voice,
        inline=False
    )
    await ctx.send(embed=embed)


Client.run(os.environ.get("TOKEN"))
