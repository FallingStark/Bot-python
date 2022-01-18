from random import choice
import discord
from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

guild_ids = [931617834298118234, 528138762006560789]


class Slash_misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="hug",
        description="hug someone",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="user",
                required=True,
                description="choose user",
                option_type=6
            )
        ]
    )
    async def hug(self, ctx: SlashContext, user: discord.Member):
        list_gif = [
            "https://cdn.weeb.sh/images/HyNJIaVCb.gif",
            "https://cdn.weeb.sh/images/HytoudXwW.gif",
            "https://cdn.weeb.sh/images/rJaog0FtZ.gif",
            "https://cdn.weeb.sh/images/r1R3_d7v-.gif"
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
                name="user",
                required=True,
                description="choose user",
                option_type=6
            )
        ]
    )
    async def wasted(self, ctx: SlashContext, user: discord.Member):
        list_gif = [
            "https://cdn.weeb.sh/images/B1VnoJFDZ.gif",
            "https://cdn.weeb.sh/images/B1qosktwb.gif",
            "https://cdn.weeb.sh/images/BJO2j1Fv-.gif",
            "https://cdn.weeb.sh/images/r11as1tvZ.gif"
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
                name="user",
                required=True,
                description="choose user",
                option_type=6
            )
        ]
    )
    async def pat(self, ctx: SlashContext, user: discord.Member):
        list_gif = [
            "https://cdn.weeb.sh/images/BkaRWA4CZ.gif",
            "https://cdn.weeb.sh/images/rkl1xJYDZ.gif",
            "https://cdn.weeb.sh/images/HyG2kJKD-.gif",
            "https://cdn.weeb.sh/images/ryh6x04Rb.gif"
        ]
        embed = discord.Embed(
            title=f"{ctx.author.display_name} fait une caresse à {user.display_name}"
        )
        embed.set_image(url=choice(list_gif))
        await ctx.send(content=f"||{user.mention}||", embed=embed)



def setup(bot):
    bot.add_cog(Slash_misc(bot))
