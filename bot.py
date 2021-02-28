import discord
import os
from discord.ext import commands

def auth(ctx):
    with open('author.txt', 'r') as f:
        lines = f.readlines()
        return ctx.author.id == int(lines[1].strip())

def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[1].strip()

intents = discord.Intents.default()

#remove if no need
intents.members = True 
intents.presences = True

client = commands.Bot(command_prefix = '!', intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.check(auth)
async def reload(ctx, extension=None):
    try:
        await ctx.message.delete()

        if extension == None:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    client.unload_extension(f'cogs.{filename[:-3]}')
                    client.load_extension(f'cogs.{filename[:-3]}')
                    print(f' <SYSTEM>  {filename[:-3]} module reloaded!')
            await ctx.send(f'`<SYSTEM>` All modules reloaded!')
        else:
            client.unload_extension(f'cogs.{extension}')
            client.load_extension(f'cogs.{extension}')
            print(f' <SYSTEM>  {extension} module reloaded!')
            await ctx.send(f'`<SYSTEM>` "{extension}" module reloaded!')
    except Exception as E:
        print(E) 

@client.command()
@commands.check(auth)
async def load(ctx, extension):
    try:
        await ctx.message.delete()
        
        client.load_extension(f'cogs.{extension}')
        print(f' <SYSTEM>  {extension} module loaded!')
        await ctx.send(f'`<SYSTEM>` "{extension}" module loaded!')
    except Exception as E:
        print(E) 

@client.command()
@commands.check(auth)
async def unload(ctx, extension):
    try:
        await ctx.message.delete()

        client.unload_extension(f'cogs.{extension}')
        print(f' <SYSTEM>  {extension} module unloaded!')
        await ctx.send(f'`<SYSTEM>` "{extension}" module unloaded!')
    except Exception as E:
        print(E) 


#You can !reload/!load/!unload Cogs
#example: !reload Basic

token = read_token()
client.run(token)
