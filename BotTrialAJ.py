import discord
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix='aj!', description='Auyyyyyyyyye')

@bot.event

async def on_ready():
    print ("Logged in as")
    print(bot.user.name)


@bot.command()
async def hello():
    await bot.say("Hello")


@bot.listen()
async def




bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")

