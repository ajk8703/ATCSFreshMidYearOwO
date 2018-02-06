import discord
import asyncio
import random

from Riddle import Riddle

client = discord.Client()

Riddle = Riddle(client)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

Riddle.run()

client.run('NDAxMDgzMDkwNTI2Nzk3ODM2.DTlBiA.rCG3a-d581NCsyFQw75_8RYBJ_M')