class cutechat (object):

    def __init__(self, client):
        self.client = client

    def run(self):
       @self.client.event
       async def on_message(message):
        if message.content.startswith('!ping'):
            await self.client.send_message(message.channel, 'Pong!')
        elif message.content.startswith("!randomcute"):
            await self.client.send_message(message.channel,
                                      'https://media.mnn.com/assets/images/2010/02/baby-orangutan.jpg.1000x0_q80_crop-smart.jpg')