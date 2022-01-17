from distutils import command
import logging
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class admin_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ar")
    async def add_role(self, ctx):
        print("j'ai adds des roles")

    @commands.command(name="kick", pass_context=True)
    @has_permissions(manage_roles=True, ban_members=True)
    async def _kick(self, ctx, member: discord.Member):
        await self.bot.kick(member)

    @_kick.error
    async def kick_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that!".format(
                ctx.message.author
            )
            await self.bot.send_message(ctx.message.channel, text)
        else:
            print("y'a un bleme")
            print(error)


def setup(bot):
    bot.add_cog(admin_commands(bot))
