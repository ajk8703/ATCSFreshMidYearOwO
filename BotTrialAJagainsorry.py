import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description='Auyyyyyyyyye')
client = discord.Client()

@client.event
async def imsad():
    await bot.say


"""
@client.event
async def on_message(message):
        # read the message that is sent.
    if message.content():
        await client.send_message(message.channel, 'Pong!')
                                        # tells you to send it to the channel that the message was sent into
"""


