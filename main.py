"""Discord bot with python"""

from datetime import datetime
import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

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

Client = commands.Bot(command_prefix="", description=DESCRIPTION, intents=intents)


@Client.command(name="tt")
async def test(ctx):
    print(Client.guilds)


@Client.command()
async def KillBot(ctx):
    await ctx.send(f"Pourquoi m'a tu tué {ctx.author.name}")
    await Client.close()


@Client.command()
async def aboutme(ctx, member: discord.Member):
    def format_date(date_raw):
        date_formater = datetime.strptime(str(date_raw), "%Y-%m-%d %H:%M:%S.%f")
        date_formated = date_formater.strftime("le %d/%m/%Y à %Hh%M et %Ss")
        return date_formated

    author_created_at = format_date(member.created_at)
    author_joined_at = format_date(member.joined_at)

    role_list = ", ".join([str(r.name) for r in member.roles])

    embed = discord.Embed(
        title=f"Infos sur {member.name}",
        description=f"Voici les infos sur {member.name}",
    )
    embed.set_thumbnail(url=member.avatar_url).add_field(
        name="Dates :",
        value=f"Date de creation : {author_created_at} \n Date de join au serv : {author_joined_at}",
        inline=False,
    ).add_field(
        name="Roles sur ce serveur :", value=f"{role_list}", inline=False
    ).add_field(
        name="Id", value=member.id, inline=False
    ).add_field(
        name="Voice", value=member.voice, inline=False
    )
    await ctx.send(embed=embed)


for file in os.listdir("./category"):  # lists all the cog files inside the cog folder.
    if file.endswith(".py"):  # It gets all the cogs that ends with a ".py".
        name = file[:-3]  # It gets the name of the file removing the ".py"
        Client.load_extension(f"category.{name}")  # This loads the cog.

Client.run(os.environ.get("TOKEN"))
