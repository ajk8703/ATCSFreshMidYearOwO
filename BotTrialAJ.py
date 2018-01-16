import discord
import asyncio
from discord.ext import commands

client = discord.Client()


class ting(object):
    """
    class Talk(object):
        def
    """
    bot = commands.Bot(command_prefix='.', description='Auyyyyyyyyye')
    @bot.event

    async def on_ready(self):
        print ("Logged in as")
        print(self.bot.user.name)


    @bot.command()
    async def talk(self):
        await self.bot.say("""
        You can talk to me! Here are the commands you can use with me!
        
        .talk -- tell me anything!
        .""")

    @bot.command()
    async def ving(self):
        await self.bot.say("Hi! How are you?")


@client.event
async def on_message(message):
    if message.content.startswith("!asd"):
        await client.send_message(message.channel, 'awwww tell me why!')


"""
@client.event
async def on_message(message):
        # read the message that is sent.
    if message.content():
        await client.send_message(message.channel, 'Pong!')
                                        # tells you to send it to the channel that the message was sent into
"""




bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")


"""keyboardsmashfeature"""