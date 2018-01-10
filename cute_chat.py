
import random
class cutechat (object):

    def __init__(self, client):
        self.client = client

    def run(self):
       @self.client.event
       async def on_message(message):
        if message.content.startswith('!ping'):
            await self.client.send_message(message.channel, 'Pong!')
        elif message.content.startswith("!randomcute"):

            image_file = open("images")
            imlist = []
            for line in image_file:
                imlist.append(line)

            randlink = imlist[random.randint(0, len(imlist))]

            await self.client.send_message(message.channel, randlink)