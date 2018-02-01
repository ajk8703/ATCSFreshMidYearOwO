import discord

from Amani.Criminal import Criminal

client = discord.Client()

Criminal = Criminal(client)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

Criminal.run()

client.run('NDAxMDgzMDkwNTI2Nzk3ODM2.DTlBiA.rCG3a-d581NCsyFQw75_8RYBJ_M')