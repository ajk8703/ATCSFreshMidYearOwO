import discord
import asyncio
#this will handle tic tac toe

class ttt (object):
    def __init__(self):

        self.clientevent()








    def clientevent(self):
        self.client = discord.Client()



        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')

        self.mode = 1

        @self.client.event
        async def on_message(message):

            if self.mode == 1:
                self.lineA = ["   ", "   ", "   "]
                self.lineB = ["   ", "   ", "   "]
                self.lineC = ["   ", "   ", "   "]
                self.listoflines = [self.lineA, self.lineB, self.lineC]


                if message.content.startswith("!ttt"):
                    self.mode = 2
                    turn = 1
                    await self.client.send_message(message.channel, "Tic Tac Toe!")
                    await self.client.send_message(message.channel, ("_ A B C\n1  %s\n2 %s\n3 %s" % ((self.lineA[0] + self.lineA[1] + self.lineA[2]),(self.lineB[0] + self.lineB[1] + self.lineB[2]),(self.lineC[0] + self.lineC[1] + self.lineC[2]))))


            elif self.mode == 2:
                char = "X"
                if message.content.startswith("!place"):
                    message1 = message.content
                    message1 = message1.split()
                    if len(message1) == 3:
                        if message1[1] == "A" or "B" or "C":
                            if int(message1[2]) == 1 or 2 or 3:
                                line = int(message1[2]) - 1

                                if message1[1] == "A":
                                    lineval = 0
                                elif message1[1] == "B":
                                    lineval = 1
                                elif message1[1] == "C":
                                    lineval = 2


                                tester = self.listoflines[line]
                                tester = tester[lineval]
                                print (tester)
                                if  ("X" in tester) or ("O" in tester):
                                    await self.client.send_message(message.channel, "That place is already taken!")

                                else:

                                    (self.listoflines[line])[lineval] = char
                                    await self.client.send_message(message.channel, ("_ A B C\n1  %s\n2 %s\n3 %s" % (
                                        (self.lineA[0] + self.lineA[1] + self.lineA[2]),
                                        (self.lineB[0] + self.lineB[1] + self.lineB[2]),
                                        (self.lineC[0] + self.lineC[1] + self.lineC[2]))))

                                    if (self.lineA[0] == self.lineA[1] and self.lineA[1] == self.lineA[2]) \
                                            or (self.lineB[0] == self.lineB[1] and self.lineB[1] == self.lineB[2]) and \
                                                            self.lineB[0] != "   " \
                                            or (self.lineC[0] == self.lineC[1] and self.lineC[1] == self.lineC[2]) and \
                                                            self.lineC[0] != "   " \
                                            or (self.lineA[0] == self.lineB[0] and self.lineC[0] == self.lineB[0]) and \
                                                            self.lineA[0] != "   " \
                                            or (self.lineA[1] == self.lineB[1] and self.lineC[1] == self.lineB[1]) and \
                                                            self.lineB[1] != "   " \
                                            or (self.lineA[2] == self.lineB[2] and self.lineC[2] == self.lineB[2]) and \
                                                            self.lineB[2] != "   " \
                                            or (self.lineA[0] == self.lineB[1] and self.lineA[0] == self.lineC[2]) and \
                                                            self.lineB[1] != "   " \
                                            or (self.lineC[0] == self.lineB[1] and self.lineA[2] == self.lineB[1]) and \
                                                            self.lineB[1] != "   ":
                                        print("Winner")
                                        await self.client.send_message(message.channel, (char + " Wins!"))
                                        self.mode = 1

                                    elif (self.lineA[0] != "   ") and (self.lineA[1] != "   ") and (
                                        self.lineA[2] != "   ") and (self.lineB[0] != "   ") and (
                                        self.lineB[1] != "   ") and (self.lineB[2] != "   ") and (
                                        self.lineC[0] != "   ") and (self.lineC[1] != "   ") and (
                                        self.lineC[2] != "   "):
                                        await self.client.send_message(message.channel, ("Board filled, no winner"))
                                        self.mode = 1



                                    if self.mode != 1:
                                        await self.client.send_message(message.channel, "O's turn!")
                                        self.mode = 3




            elif self.mode == 3:
                char = "O"
                if message.content.startswith("!place"):
                    message1 = message.content
                    message1 = message1.split()
                    if len(message1) == 3:
                        if message1[1] == "A" or "B" or "C":
                            if int(message1[2]) == 1 or 2 or 3:
                                line = int(message1[2]) - 1

                                if message1[1] == "A":
                                    lineval = 0
                                elif message1[1] == "B":
                                    lineval = 1
                                elif message1[1] == "C":
                                    lineval = 2


                                tester = self.listoflines[line]
                                tester = tester[lineval]
                                if ("X" in tester) or ("O" in tester):

                                    await self.client.send_message(message.channel, "That place is already taken!")



                                else:

                                    (self.listoflines[line])[lineval] = char
                                    await self.client.send_message(message.channel, ("_ A B C\n1  %s\n2 %s\n3 %s" % (
                                        (self.lineA[0] + self.lineA[1] + self.lineA[2]),
                                        (self.lineB[0] + self.lineB[1] + self.lineB[2]),
                                        (self.lineC[0] + self.lineC[1] + self.lineC[2]))))




                                    print(self.lineA[0],self.lineA[1],self.lineA[2])
                                    if (self.lineA[0] == self.lineA[1] and self.lineA[1] == self.lineA[2]) \
                                            or (self.lineB[0] == self.lineB[1] and self.lineB[1] == self.lineB[2]) and self.lineB[0] != "   "\
                                            or (self.lineC[0] == self.lineC[1] and self.lineC[1] == self.lineC[2]) and self.lineC[0] != "   "\
                                            or (self.lineA[0] == self.lineB[0] and self.lineC[0] == self.lineB[0]) and self.lineA[0] != "   "\
                                            or (self.lineA[1] == self.lineB[1] and self.lineC[1] == self.lineB[1]) and self.lineB[1] != "   "\
                                            or (self.lineA[2] == self.lineB[2] and self.lineC[2] == self.lineB[2]) and self.lineB[2] != "   "\
                                            or (self.lineA[0] == self.lineB[1] and self.lineA[0] == self.lineC[2]) and self.lineB[1] != "   "\
                                            or (self.lineC[0] == self.lineB[1] and self.lineA[2] == self.lineB[1]) and self.lineB[1] != "   ":


                                        print("Winner")
                                        await self.client.send_message(message.channel, (char + " Wins!"))
                                        self.mode = 1

                                    elif (self.lineA[0] != "   ") and (self.lineA[1] != "   ") and (
                                        self.lineA[2] != "   ") and (self.lineB[0] != "   ") and (
                                        self.lineB[1] != "   ") and (self.lineB[2] != "   ") and (
                                        self.lineC[0] != "   ") and (self.lineC[1] != "   ") and (
                                        self.lineC[2] != "   "):
                                        await self.client.send_message(message.channel, ("Board filled, no winner"))
                                        self.mode = 1

                                    if self.mode != 1:
                                        await self.client.send_message(message.channel, "X's turn!")
                                        self.mode = 2





        self.client.run('Mzk5OTg1ODQ4NzIxOTk3ODM0.DTVDcA.7T0LiBlo5aaq7MQXWclQ6lJTzPw')


ttt = ttt()