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
                name="name",
                required=True,
                description="choose module",
                option_type=3,
                choices=[
                    create_choice(name="events", value="events"),
                    create_choice(name="misc", value="misc"),
                    create_choice(name="admin", value="admin"),
                ],
            )
        ],
    )
    async def reload(self, ctx: SlashContext, name: str):
        if any(str(ctx.author.id) in str(id) for id in self.bot.owner_ids):
            logging.info(f"Reloading : '{name}'")
            try:
                self.bot.reload_extension(f"category.{name}")
            except Exception as e:
                logging.error(e)
                return await ctx.send(e)
            logging.info(f"'{name}' was reloaded")
            await ctx.send(f'"**{name}**" was reloaded')
        else:
            await ctx.send(
                """
                    Tu n'a pas la permission d'utilisé cette commande, seul les devs authorisés ont le droit de l'utilisé
                """
            )

    @cog_ext.cog_slash(
        name="unload",
        description="unload module",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="name",
                required=True,
                description="choose module",
                option_type=3,
                choices=[
                    create_choice(name="events", value="events"),
                    create_choice(name="misc", value="misc"),
                    create_choice(name="admin", value="admin"),
                ],
            )
        ],
    )
    async def unload(self, ctx: SlashContext, name: str):
        if any(str(ctx.author.id) in str(id) for id in self.bot.owner_ids):
            logging.warn(f"Unloading : '{name}'")
            try:
                self.bot.unload_extension(f"category.{name}")
            except Exception as e:
                return await ctx.send(e)
            logging.warn(f"'{name}' was unloaded")
            await ctx.send(f'"**{name}**" was unloaded')
        else:
            await ctx.send(
                """
                    Tu n'a pas la permission d'utilisé cette commande, seul les devs authorisés ont le droit de l'utilisé
                """
            )

    @cog_ext.cog_slash(
        name="load",
        description="load module",
        guild_ids=guild_ids,
        options=[
            create_option(
                name="name",
                required=True,
                description="choose module",
                option_type=3,
                choices=[
                    create_choice(name="events", value="events"),
                    create_choice(name="misc", value="misc"),
                    create_choice(name="admin", value="admin"),
                ],
            )
        ],
    )
    async def load(self, ctx: SlashContext, name: str):
        if any(str(ctx.author.id) in str(id) for id in self.bot.owner_ids):
            logging.info(f"Loading : '{name}'")
            try:
                self.bot.load_extension(f"category.{name}")
            except Exception as e:
                return await ctx.send(e)
            logging.info(f"'{name}' was loaded")
            await ctx.send(f'"**{name}**" was loaded')
        else:
            await ctx.send(
                """
                    Tu n'a pas la permission d'utilisé cette commande, seul les devs authorisés ont le droit de l'utilisé
                """
            )

    @cog_ext.cog_slash(
        name="module", guild_ids=guild_ids, description="give all module name"
    )
    async def _module(self, ctx: SlashContext):
        if any(str(ctx.author.id) in str(id) for id in self.bot.owner_ids):
            list_extensions = []
            for extension in self.bot.extensions:
                list_extensions.append(extension)

            await ctx.send(", ".join(list_extensions))
        else:
            await ctx.send(
                """
                    Tu n'a pas la permission d'utilisé cette commande, seul les devs authorisés ont le droit de l'utilisé
                """
            )

    @cog_ext.cog_slash(name="ping", guild_ids=guild_ids, description="give ping of bot")
    async def _ping(self, ctx: SlashContext):
        await ctx.send(f"Ping : {self.bot.latency*1000}ms")
        with open("")
        print("-----Users-----")
        for user in self.bot.users:
            print(user)
        print("-----Guilds-----")
        for guild in self.bot.guilds:
            print(guild)


def setup(bot):
    bot.add_cog(Slash(bot))
