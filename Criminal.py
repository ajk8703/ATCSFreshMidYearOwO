class Criminal (object):
    def __init__ (self, client):
        self.client = client
        self.mode = 0

    def run(self):

        @self.client.event
        async def on_message(message):
            if self.mode == 0:
                if message.content.startswith('!criminal'):
                    self.mode = 1
                    await self.client.send_message(message.channel, "A man died in his round house. The butcher said he was chopping meat. "
                                                                    "The gardener said she was pulling weeds. "
                                                                    "The butler said he was dusting the corners. Who killed the man?")

            elif self.mode == 1:

                if message.content.startswith("!gardener"):
                    await self.client.send_message(message.channel, 'Wrong!')

                elif message.content.startswith("!butcher"):
                    await self.client.send_message(message.channel, 'Wrong!')

                elif message.content.startswith("!butler"):
                    await self.client.send_message(message.channel, 'Correct! The house has NO corners!')

                self.mode = 0