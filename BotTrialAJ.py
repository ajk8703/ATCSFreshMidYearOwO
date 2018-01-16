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

@client.event
async def on_message(message):
    if message.content.startswith(".imsad"):
        await client.send_message(message.channel, 'awwww tell me why!')


"""
@client.event
async def on_message(message):
        # read the message that is sent.
    if message.content():
        await client.send_message(message.channel, 'Pong!')
                                        # tells you to send it to the channel that the message was sent into
"""




bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")


"""keyboardsmashfeature"""