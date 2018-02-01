import discord
import asyncio
import time

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!story1'):
        s =  ['hi']

        for i in s:
            await client.send_message(message.channel, s)
            time.sleep(2)

    if message.content.startswith('!story2'):
        s =



client.run('Mzk5OTg1ODQ4NzIxOTk3ODM0.DTVDcA.7T0LiBlo5aaq7MQXWclQ6lJTzPw')
