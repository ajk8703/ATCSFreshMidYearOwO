import discord
import asyncio
from discord.ext import commands

"""
class Talk(object):
    def 
"""
bot = commands.Bot(command_prefix='.', description='Auyyyyyyyyye')
client = discord.Client()
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




bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")


"""keyboardsmashfeature"""