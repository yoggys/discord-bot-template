from functions.Logger import log_info, error_handle
from discord.ext import commands
import sys

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #on_ready event example
    @commands.Cog.listener()
    async def on_ready(self):
        log_info("Basic module loaded!")
        # TODO: declare self variables, start task loops here etc.
    
    #on_command_error event example
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            async def notify(info):
                await ctx.send(f":exclamation: {info.capitalize()}!")

            if isinstance(error, commands.MissingRequiredArgument):
                await notify('please provide all required arguments')
            if isinstance(error, commands.CommandOnCooldown):
                await notify('this command is on cooldown, please try again in {:.2f}s'.format(error.retry_after))
            # TODO: add more error handling if you want
        except Exception as E:
                error_handle("ERROR", f"{self.__class__.__name__} - {sys._getframe().f_code.co_name}", E)

    #on_message event example
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            pass
            #do something with message
        except Exception as E:
                error_handle("ERROR", f"{self.__class__.__name__} - {sys._getframe().f_code.co_name}", E)
   
    #command example
    @commands.command()
    async def test(self, ctx): #replace test with command name
        try:
            pass
            # TODO: do what you want
        except Exception as E:
                error_handle("ERROR", f"{self.__class__.__name__} - {sys._getframe().f_code.co_name}", E)

    #check bot ping
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user) #command cooldown for user
    async def status(self, ctx):
        try:
            await ctx.send(f':white_check_mark: Working {round(self.client.latency * 1000)}ms')
        except Exception as E:
                error_handle("ERROR", f"{self.__class__.__name__} - {sys._getframe().f_code.co_name}", E)

def setup(client):
    client.add_cog(Basic(client))
