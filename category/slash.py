from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import logging

guild_ids = [931617834298118234, 528138762006560789]


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="reload",
        description="reload module",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="option",
                required=True,
                description="choose module",
                option_type=3,
                choices=[
                    create_choice(name="events", value="events"),
                    create_choice(name="misc", value="misc"),
                    create_choice(name="manage commands", value="manage_commands"),
                    create_choice(name="admin", value="admin"),
                ],
            )
        ],
    )
    async def ping(self, ctx: SlashContext, option: str):
        if ctx.author.id == 212593654819323904:
            logging.info(f"Reloading : '{option}'")
            try:
                self.bot.reload_extension(f"category.{option}")
            except Exception as e:
                logging.error(e)
                return await ctx.send(e)
            logging.info(f"'{option}' was reloaded")
            await ctx.send(f'"**{option}**" was reloaded')
        else:
            await ctx.send(
                """
                    Tu n'a pas la permission d'utilisé cette commande, seul les devs authorisés ont le droit de l'utilisé
                """
            )

    @cog_ext.cog_slash(name="ping", guild_ids=guild_ids)
    async def _ping(self, ctx: SlashContext):
        await ctx.send(f"Pong! ({self.bot.latency*1000}ms)")

    @cog_ext.cog_subcommand(base="group", name="say", guild_ids=guild_ids)
    async def group_say(self, ctx: SlashContext, text: str):
        await ctx.send(content=text)


def setup(bot):
    bot.add_cog(Slash(bot))
