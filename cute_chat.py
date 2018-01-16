import discord
import asyncio
import random


#we will remove the #'s when youtube and games work
#from youtube_chat import youtube_chat
#from games_chat import games_chat

client = discord.Client()


@client.event
async def on_message(message):

        if message.content.startswith('!randomcute'):

            imagefile = open("images")
            imlist = []
            for line in imagefile:
                imlist.append(line)
            use = imlist[random.randint(0, len(imlist))]

            await client.send_message(message.channel,use)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')




#we will remove the #'s when youtube and games work
#youtube_chat.run()
#games_chat.run()






client.run('Mzk5OTg1ODQ4NzIxOTk3ODM0.DTVDcA.7T0LiBlo5aaq7MQXWclQ6lJTzPw')