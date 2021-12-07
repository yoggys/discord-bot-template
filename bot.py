from functions.Logger import init_logger, log_info, error_handle
from discord.ext import commands
from dotenv import load_dotenv
from discord import Intents
import sys
import os

load_dotenv(override=True)
init_logger()

intents = Intents.default()
intents.members = True 
intents.presences = True
intents.messages = True

client = commands.Bot(command_prefix = '!', intents=intents)

# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

AUTHOR = int(os.getenv('AUTHOR'))
def auth(ctx):
    return ctx.message.author.id == AUTHOR

"""
    System commands
    You can !reload/!load/!unload Cogs
    example: !reload Basic
"""
@client.command()
@commands.check(auth)
async def reload(ctx, extension=None):
    try:
        if extension == None:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    client.unload_extension(f'cogs.{filename[:-3]}')
                    client.load_extension(f'cogs.{filename[:-3]}')
                    log_info(f'{filename[:-3]} module reloaded!')
            await ctx.send(f'`<SYSTEM>` All modules reloaded!')
        else:
            client.unload_extension(f'cogs.{extension}')
            client.load_extension(f'cogs.{extension}')
            log_info(f'{extension} module reloaded!')
            await ctx.send(f'`<SYSTEM>` "{extension}" module reloaded!')
    except Exception as E:
        error_handle("ERROR", f"INIT - {sys._getframe().f_code.co_name}", E)

@client.command()
@commands.check(auth)
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        log_info(f'{extension} module loaded!')
        await ctx.send(f'`<SYSTEM>` "{extension}" module loaded!')
    except Exception as E:
        error_handle("ERROR", f"INIT - {sys._getframe().f_code.co_name}", E)


@client.command()
@commands.check(auth)
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        log_info(f'{extension} module unloaded!')
        await ctx.send(f'`<SYSTEM>` "{extension}" module unloaded!')
    except Exception as E:
        error_handle("ERROR", f"INIT - {sys._getframe().f_code.co_name}", E)

TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
