import discord
import asyncio

import random
print("lets play\n")
up = 0
cp = 0
while up <= 5 and cp <= 5:
    if up == 5 or cp == 5:
        break

    user = input("\npick 'r'ock, 'p'aper, 's'cissors")
    comp = random.choice(["r", "p", "s"])

    if user == "r" and comp == "s":
        up += 1
    elif user == "s" and comp == "p":
        up += 1
    elif user == "p" and comp == "r":
        up += 1
    elif user == comp:
        up = up
    else:
        cp += 1

    print ("You chose %s and the OwO chose %s\n\nThe score is now:\n\tYou %d\n\tOwO %d" % (user, comp, up, cp))

if up == 5:
    print("\nwowww :3 you win !!! i'm pwoud ")
else:
    print("\nhehehe I winnn !!! bettew wuck next time")
