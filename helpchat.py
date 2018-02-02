import discord
import asyncio
import random



client = discord.Client()


@client.event
async def on_message(message):

        if message.content.startswith('!help'):



            await client.send_message(message.channel, "!rps: rock paper scissors, use !rock, !paper, or !scissors when running\n\n!randomcute: adds a random cute image to chat\n\n!help: help\n\n!ttt: tic tac toe, place X's and O's with !place followed by letter, then number coordinate")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')








client.run('Mzk5OTg1ODQ4NzIxOTk3ODM0.DTVDcA.7T0LiBlo5aaq7MQXWclQ6lJTzPw')