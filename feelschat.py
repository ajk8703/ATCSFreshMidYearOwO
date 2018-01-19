

#this will handle feels
import discord
import asyncio



client = discord.Client()


@client.event
async def on_message(message):

        if " sad" in message.content:
            await client.send_message(message.channel, "The feelsbar is open: https://i.ytimg.com/vi/BpX8E-kavmI/maxresdefault.jpg")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')








client.run('Mzk5OTg1ODQ4NzIxOTk3ODM0.DTVDcA.7T0LiBlo5aaq7MQXWclQ6lJTzPw')