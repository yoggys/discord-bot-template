from discord.ext import commands, tasks

from utils.client import MyBot
import discord


class Base(commands.Cog):
    def __init__(self, client: MyBot) -> None:
        self.client = client
        self.count = 0

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Cog Base is ready.")

        if not self.count_loop.is_running():
            self.count_loop.start()

    @tasks.loop(minutes=1.0)
    async def count_loop(self) -> None:
        print(f"Count: {self.count}")
        count += 1

    @commands.slash_command(description="Get the bot's latency.")
    async def ping(self, ctx: discord.ApplicationContext) -> None:
        latency = round(self.client.latency * 1000)
        await ctx.respond(f"Pong! {latency}ms", ephemeral=True)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        print(f"{message.author}: {message.content}")

    @commands.user_command(name="Get avatar", description="Get a user's avatar.")
    async def avatar(self, ctx: discord.ApplicationContext, user: discord.User) -> None:
        embed = discord.Embed(
            title=f"{user.name}'s avatar", color=discord.Color.blurple()
        )
        embed.set_image(url=user.display_avatar)
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.message_command(
        name="Count characters and words",
        description="Count the characters and words in a message.",
    )
    async def count_characters(
        self, ctx: discord.ApplicationContext, message: discord.Message
    ) -> None:
        words = len(message.content.split(" "))
        characters = len(message.content)
        await ctx.respond(f"Words: {words}\nCharacters: {characters}", ephemeral=True)


def setup(client):
    client.add_cog(Base(client))
