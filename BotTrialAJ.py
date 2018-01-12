import discord
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix='a!', description='Auyyyyyyyyye')

@bot.event

async def on_ready():
    print ("Logged in as")
    print(bot.user.name)


@bot.command()
async def hello():
    await bot.say("no")

@bot.command()
async def ving():
    await bot.say("Hi! How are you?")

@bot.command()
async def say(something):
    await bot.say(something)

"""
@client.event
async def



@bot.listen()
async def
"""




bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")

