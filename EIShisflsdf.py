import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='smash', description='Auyyyyyyyyye')

alpha = open("Alphabet", "r")
alphaplus = open("morethanalphabet", "r")
meep = ""
bean = ""
for x in alpha:
    x = x.strip("\n")
    meep += x
    bean += x
for r in alphaplus:
    r = r.strip("\n")
    bean += r



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

    await bot.say((ergh).upper())


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

@bot.command()
async def a(something):
    something = int(something)
    if something > 2000:
        await bot.say("Heyyyy calm down there")
    ergh = ""
    for i in range(something):
        i = random.choice(bean)
        ergh += i

    await bot.say(ergh)


@bot.command()
async def a(something):
    something = int(something)
    if something > 2000:
        await bot.say("Heyyyy calm down there")
    ergh = ""
    for i in range(something):
        i = random.choice(meep)
        ergh += i

    await bot.say(ergh)

"""
import random
import string

def command(x):
    keylist = [random.choice(string.ascii_letters) for i in range(x)]
    return ("".join(keylist))

print(command(5))

"""
"""
@client.event
async def on_message(message):
        # read the message that is sent.
    if message.content():
        await client.send_message(message.channel, 'Pong!')
                                        # tells you to send it to the channel that the message was sent into
"""

bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")

