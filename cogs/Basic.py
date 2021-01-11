import discord
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import BucketType, CooldownMapping

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #on_ready event example
    @commands.Cog.listener()
    async def on_ready(self):
        print('<STARTUP> Test module loaded!')
    
    #on_command_error event example
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            mess = await ctx.send(':exclamation: Please provide all required arguments!')
            await asyncio.sleep(10)
            await mess.delete()
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            mess = await ctx.send(':exclamation: This command is on cooldown, please try again in {:.2f}s'.format(error.retry_after))
            await asyncio.sleep(5)
            await mess.delete()

    #on_message event example
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            pass
            #do something with message
        except Exception as E:
            print(E)
   
    #command example
    @commands.command()
    async def test(self, ctx): #replace test with command name
        try:
            pass
            #do something
        except Exception as E:
            print(E)

    #check bot ping
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user) #command cooldown for user
    async def status(self, ctx):
        try:
            await ctx.message.delete()
            await ctx.send(f':white_check_mark: Working {round(self.client.latency * 1000)}ms')
        except Exception as E:
            print(E)

def setup(client):
    client.add_cog(Basic(client))
