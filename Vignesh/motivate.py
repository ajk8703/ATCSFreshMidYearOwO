import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!imsad'):
        x = ['You awe wondewfuw :)', 'You awe gweat', 'You awe so woved', 'You can do it!', 'You awe so wovewy <3', 'Things wiww get bettew :), ']
        await client.send_message(message.channel, random.choice(x))


client.run('Mzk5OTg1ODQ4NzIxOTk3ODM0.DTVDcA.7T0LiBlo5aaq7MQXWclQ6lJTzPw')