import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='smash', description='Auyyyyyyyyye')

alpha = open("Alphabet", "r")
meep = ""
for x in alpha:
    x = x.strip("\n")
    meep += x


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)


@bot.command()
async def u(something):
    something = int(something)
    if something > 2000:
        await bot.say("Heyyyy calm down there")
    ergh = ""
    for i in range(something):
        i = random.choice(meep)
        ergh += i

    await bot.say(ergh)


@bot.command()
async def l(something):
    something = int(something)
    if something > 2000:
        await bot.say("Heyyyy calm down there")
    ergh = ""
    for i in range(something):
        i = random.choice(meep)
        ergh += i

    await bot.say((ergh).lower())



"""
@client.event
async def on_message(message):
        # read the message that is sent.
    if message.content():
        await client.send_message(message.channel, 'Pong!')
                                        # tells you to send it to the channel that the message was sent into
"""

bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")

