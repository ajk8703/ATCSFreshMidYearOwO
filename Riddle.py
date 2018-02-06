import random

class Riddle (object):
    def __init__ (self, client):
        self.client = client
        self.mode = 0

    def run(self):

        @self.client.event
        async def on_message(message):
            if message.content.startswith('!riddle'):
                riddlesFile = open("Riddles","r")
                answersFile = open("Ans","r")
                riddles = []
                answers = []



                for line in riddlesFile:
                    riddles.append(line)

                for line in answersFile:
                    answers.append(line)

                key = random.randint(0, len(riddles)-1)

                quest = riddles[key]
                self.answer = answers[key]
                await self.client.send_message(message.channel, quest)


                self.mode = 1
                if self.mode == 1:
                    await self.client.send_message(message.channel, "Bet you didn't guess %s" % (self.answer))
                    self.mode = 0