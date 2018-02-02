# DONEEEEEE


import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix='smash', description='Ayyyyye')
client = discord.Client()

bot.remove_command('help')

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


@bot.command()
async def help():
    await bot.say("""```Ayyyyye looking to keyboard smash with ease? ༼ つ ❍_❍ ༽つ 

To use this bot, type smash[] {}. Fill the {} with a number and the [] with one of the following letters:

  u    = FOR AN UPPERCASE KEYBOARD SMASH *composed of only letters*
  l    = for an lowercase keyboard smash *composed of only letters*
  b    = For A raNdom KEyboaRd sMaSH *composed of only letters*
  e    = F0r @ k3yB0@rd Sm@sh *composed with letters and numbers/symbols*

Type smashhelp command for more info on a command. I'd be more than happy to assist you! Ꮚ•ꈊ•Ꮚ```""")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)


@bot.command()
async def u(something):
    '''= FOR AN UPPERCASE KEYBOARD SMASH *composed of only letters*'''
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
    '''= for an lowercase keyboard smash *composed of only letters*'''
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
    '''= For A raNdom KEyboaRd sMaSH *composed of only letters*'''
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
    '''= F0r @ k3yB0@rd Sm@sh *composed with letters and numbers/symbols*'''
    anything = int(anything)
    ergh = ""
    for i in range(anything):
        i = random.choice(bean)
        ergh += i

    await bot.say(ergh)



bot.run("Mzk5OTg1ODQ4NzIxOTk3ODM0.DTVDcA.7T0LiBlo5aaq7MQXWclQ6lJTzPw")
