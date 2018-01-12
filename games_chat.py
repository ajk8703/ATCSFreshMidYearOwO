#this will handle in-chat games
import random
class games_chat (object):
    def __init__ (self, client):
        self.client = client
        self.mode = 0
    def run(self):




        @self.client.event
        async def on_message(message):
            if self.mode == 0:
                if message.content.startswith('!rps'):
                    self.mode = 1
                    await self.client.send_message(message.channel, "Rock, Paper, Scissors...")
                if message.content.startswith('!ttt'):
                    self.mode = 2




            elif self.mode == 1:
            #this does everything for rock paper scissors



                computer = random.randint(1,3)
                if computer == 1:
                    computer = "rock"
                elif computer == 2:
                    computer = "paper"
                elif computer == 3:
                    computer = "scissors"

                if message.content.startswith("!rock"):
                    player = "rock"
                elif message.content.startswith("!paper"):
                    player = "paper"
                elif message.content.startswith("!scissors"):
                    player = "scissors"

                if computer == player:
                    await self.client.send_message(message.channel, 'Tie!')

                elif computer == "rock":
                    if player == "paper":
                        await self.client.send_message(message.channel, 'you win D:')
                    else:
                        await self.client.send_message(message.channel, 'I win! :D')

                elif computer == "paper":
                    if player == "rock":
                        await self.client.send_message(message.channel, 'I win! :D')
                    else:
                        await self.client.send_message(message.channel, 'you win D:')

                elif computer == "scissors":
                    if player == "rock":
                        await self.client.send_message(message.channel, 'you win D:')
                    elif player == "paper":
                        await self.client.send_message(message.channel, 'I win! :D')

                await self.client.send_message(message.channel, "You threw " + player + ", I threw " + computer)
                self.mode = 0
