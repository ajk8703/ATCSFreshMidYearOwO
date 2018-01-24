import discord
import time

client = discord.Client()



@client.event
async def on_message(message):

        if message.content.startswith('=s=murder'):
            await client.send_message(message.channel, """You woke up, startled in your bed. A night of fitful unrest coupled with nightmares brought you to a cold sweat. A creak can be heard from outside your bedroom door... you startle. Will you...
            (=murder1) Get out of bed and open the bedroom door
            (=murder2) Duck under your covers for safety and stay as quiet as possible
            (=murder3) Crawl out the window""")
            if message.content.startswith('=murder1'):
                await client.send_message(message.channel, "")
            if message.content.startswith('=murder2'):
                await client.send_message(message.channel, "")
            if message.content.startswith("=murder3"):
                await client.send_message(message.channel, "")




client.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")
