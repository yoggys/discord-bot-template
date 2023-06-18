import discord
from discord.ext import commands


class YogBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.all())
        self.load_extension("cogs.Base")

    async def on_ready(self) -> None:
        print("Running as {} (ID: {})".format(self.user, self.user.id))
