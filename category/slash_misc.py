from random import choice
import discord
from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from .stats import Player
import json
from datetime import datetime
import locale

guild_ids = [931617834298118234, 528138762006560789]

locale.setlocale(locale.LC_ALL, "")


class Slash_misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="hug",
        description="hug someone",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="user", required=True, description="choose user", option_type=6
            )
        ],
    )
    async def hug(self, ctx: SlashContext, user: discord.Member):
        list_gif = [
            "https://cdn.weeb.sh/images/HyNJIaVCb.gif",
            "https://cdn.weeb.sh/images/HytoudXwW.gif",
            "https://cdn.weeb.sh/images/rJaog0FtZ.gif",
            "https://cdn.weeb.sh/images/r1R3_d7v-.gif",
        ]
        embed = discord.Embed(
            title=f"{ctx.author.display_name} fait un câlin à {user.display_name}"
        )
        embed.set_image(url=choice(list_gif))
        await ctx.send(content=f"||{user.mention}||", embed=embed)

    @cog_ext.cog_slash(
        name="wasted",
        description="wasted someone",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="user", required=True, description="choose user", option_type=6
            )
        ],
    )
    async def wasted(self, ctx: SlashContext, user: discord.Member):
        list_gif = [
            "https://cdn.weeb.sh/images/B1VnoJFDZ.gif",
            "https://cdn.weeb.sh/images/B1qosktwb.gif",
            "https://cdn.weeb.sh/images/BJO2j1Fv-.gif",
            "https://cdn.weeb.sh/images/r11as1tvZ.gif",
        ]
        embed = discord.Embed(
            title=f"{user.display_name} c'est fait wasted par {ctx.author.display_name}"
        )
        embed.set_image(url=choice(list_gif))
        await ctx.send(content=f"||{user.mention}||", embed=embed)

    @cog_ext.cog_slash(
        name="pat",
        description="pat someone",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="user", required=True, description="choose user", option_type=6
            )
        ],
    )
    async def pat(self, ctx: SlashContext, user: discord.Member):
        list_gif = [
            "https://cdn.weeb.sh/images/BkaRWA4CZ.gif",
            "https://cdn.weeb.sh/images/rkl1xJYDZ.gif",
            "https://cdn.weeb.sh/images/HyG2kJKD-.gif",
            "https://cdn.weeb.sh/images/ryh6x04Rb.gif",
        ]
        embed = discord.Embed(
            title=f"{ctx.author.display_name} fait une caresse à {user.display_name}"
        )
        embed.set_image(url=choice(list_gif))
        await ctx.send(content=f"||{user.mention}||", embed=embed)

    @cog_ext.cog_slash(
        name="init",
        description="init stats lol",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="summoner_name",
                required=True,
                description="summer name",
                option_type=3,
            )
        ],
    )
    async def init(self, ctx: SlashContext, summoner_name):
        SummonerData = Player(summoner_name)
        if SummonerData.code != 200:
            print(f"Code : {SummonerData.code}")
            await ctx.send(f"Code : {SummonerData.code}")
        self.SummonerData = SummonerData
        await ctx.send("init good")

    @cog_ext.cog_slash(
        name="get_mastery_champion",
        description="get mastery lol",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="champion",
                required=True,
                description="champion name",
                option_type=3,
            )
        ],
    )
    async def get_mastery_champion(self, ctx: SlashContext, champion):
        content = self.SummonerData.get_champion_mastery(champion)
        if self.SummonerData.code != 200:
            ctx.send(f"Code : {self.SummonerData.code} Invalide champion name")
            return f"Code : {self.SummonerData.code}"
        with open("champion_id.json", "r") as file:
            file_content = file.read()
        list_champion = json.loads(file_content)
        for champion_id in list_champion:
            if int(champion_id) == content["championId"]:
                champion_name = list_champion[champion_id]

        mastery = content["championLevel"]
        mastery_points = content["championPoints"]
        last_play_timestamp = content["lastPlayTime"]
        last_play_timestamp = int(str(last_play_timestamp)[:-3])
        last_play_time = datetime.fromtimestamp(float(last_play_timestamp))
        last_play_time = last_play_time.strftime("%H:%M:%S - %d/%m/%Y")
        print("")
        print("--------------------------------------")
        print(f"{champion_name}")
        print(f"Mastery {mastery}")
        print(f"Mastery points : {mastery_points:n} pts")
        print(f"Last play time : {last_play_time}")
        print("--------------------------------------")
        print("")
        embed = (
            discord.Embed(
                title=f"Infos sur {self.SummonerData.name}",
                description=f"Voici les infos sur {champion_name}",
            )
            .add_field(name="Mastery :", value=f"{mastery}", inline=False)
            .add_field(
                name="Mastery points :", value=f"{mastery_points:n} pts", inline=False
            )
            .add_field(name="Last play time :", value=f"{last_play_time}", inline=False)
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Slash_misc(bot))
