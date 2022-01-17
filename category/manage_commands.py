import logging
from discord.ext import commands


class loading_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, *, name: str):
        logging.info(f"Reloading : '{name}'")
        try:
            self.bot.reload_extension(f"category.{name}")
        except Exception as e:
            logging.error(e)
            return await ctx.send(e)
        logging.info(f"'{name}' was reloaded")
        await ctx.send(f'"**{name}**" was reloaded')

    @commands.command()
    async def unload(self, ctx, *, name: str):
        logging.warn(f"Unloading : '{name}'")
        try:
            self.bot.unload_extension(f"category.{name}")
        except Exception as e:
            return await ctx.send(e)
        logging.warn(f"'{name}' was unloaded")
        await ctx.send(f'"**{name}**" was unloaded')

    @commands.command()
    async def load(self, ctx, *, name: str):
        logging.info(f"Loading : '{name}'")
        try:
            self.bot.load_extension(f"category.{name}")
        except Exception as e:
            return await ctx.send(e)
        logging.inf(f"'{name}' was loaded")
        await ctx.send(f'"**{name}**" was loaded')


def setup(bot):
    bot.add_cog(loading_commands(bot))
