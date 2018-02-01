import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='smash', description='Auyyyyyyyyye')

alpha = open("Alphabet", "r")
bean = ""
meep = ""
for x in alpha:
    x = x.strip("\n")
    meep += x
    bean += x

num = open("morethanalphabet", "r")
numlist = ""
for t in num:
    t = t.strip("\n")
    numlist += t
    bean += t


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
async def b(something):
    something = int(something)
    if something > 2000:
        await bot.say("Heyyyy calm down there")
    ergh = ""
    for i in range(something):
        i = random.choice(meep)
        ergh += i

    await bot.say(ergh)

@bot.command()
async def e(anything):
    anything = int(anything)
    ergh = ""
    for i in range(anything):
        i = random.choice(bean)
        ergh += i

    await bot.say(ergh)


@bot.command()
async def halp():
    await bot.say("Type \"smashu\" for an uppercase keyboard smash.\nType \"smashl\" for a lowercase keyboard smash.\nType \"smashb\" for an allcase keyboard smash.\nType \"smashe\" for an EVERYTHING keyboard smash. :3")


bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")
