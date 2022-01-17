import discord
from discord import Embed
from discord.ext import commands
from datetime import datetime


class misc_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, member: discord.Member):
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


def setup(bot):
    bot.add_cog(misc_commands(bot))
