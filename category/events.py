import discord
from discord.ext import commands
import logging


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """When client is ready"""
        logging.info(f"{self.bot.user.name} is ready")
        print(f"{self.bot.user.name} is ready")
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="raphtalia"
            )
        )

    @commands.Cog.listener()
    async def on_connect(self):
        """When client is connected to discord"""
        logging.info(f"{self.bot.user.name} is connected to discord")
        print(f"{self.bot.user.name} is connected to discord")

    @commands.Cog.listener()
    async def on_disconnect(self):
        """When client is disconnected to discord"""
        logging.info(f"{self.bot.user.name} is disconnected to discord")
        print(f"{self.bot.user.name} is disconnected to discord")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if (
            "slt" in ctx.content
            or "bonjour" in ctx.content
            or "hello" in ctx.content
            or "cc" in ctx.content
        ):
            await ctx.add_reaction("👋")


def setup(bot):
    bot.add_cog(events(bot))
