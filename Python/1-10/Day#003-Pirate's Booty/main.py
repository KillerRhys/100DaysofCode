""" Pirate's Booty!
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.01-1740 """


# INTRO
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Pirate's Booty!.")
print("Your mission is to find the treasure.\n")

quest = input("You find yourself marooned at Skull Cove durning high tide.\nBefore you lies two paths, one to the left and one to your right.\nWhich will you take? ")
quest = quest.lower()
if quest == "left":
    print("")
    q2 = input("After some walking you find the entrance to a mysterious cavern.\nAbove the entrance is a skull & crossbones with a torch nearby.\nDo you \"light\" the torch, \"continue\" on or \"wait\"? ")
    q2 = q2.lower()

    if q2 == "light":
        print("Picking up a flint you strike some embers upon the torch which catches fire!\nAs you make your way into the cavern you hear the rumble of a million insect wings.\nDarkness envelopes you as the bugs begin to feast!")

    elif q2 == "wait":
        print("You slink into the shadows and wait patiently. After some time an old sea dog makes his way to the cave.")
        print("He asks if you're looking to join his crew and decide some claim to the treasure is better than being marooned.")
        print("On the high seas you spend your days until swallowed whole by a Kraken!")

    elif q2 == "continue":
        print("")
        q3 = input("You fumble in the darkness hoping you don't break your leg or get stuck.\nIn the distance you spot an otherwordly green glow.\nYou find yourself in a room full of emeralds wall to wall.\nWill you \"Take\" what you can carry, \"Rest\" for a spell or \"Keep\" going deeper? ")
        q3 = q3.lower()
        if q3 == "take":
            print("You take out your satchel and start stuffing emeralds of all sizes into the bag.\nYou begin to realize the green around the lower half of the room is not emeralds, but large scales.\nYou make to scream as a large fanged head removes yours!")

        elif q3 == "rest":
            print("You are exhausted after all of the days trials. You lay back and sleep begins to fall over you.\nYou awake to a sharp pain in your throat gasping for air!\nThe Captain looms over you with a wicked grin!")

        elif q3 == "keep":
            print("")
            q4 = input("The will to move on and leave the beautiful gems seems other-worldly.\nThe sound of rushing water fills your ears and you become anxious.\nYou see a waterfall in the center of the cave and glints of gold & silver all around!\nWill you grab some \"Loot\", \"Turn\" and run or \"wait\"? ")
            q4 = q4.lower()

            if q4 == "loot":
                print("You can't help yourself after all you've endured it's time to collect your reward!")
                print("As you stuff handful after handful of gems, coins and artefacts in your satchel you see a large eye peering up from the pool")
                print("Suddenly you find yourself upside down in the Kraken's grasp as you're pulled towards a snapping beak!")

            elif q4 == "turn":
                print("Your anxiety gets the better of you and you turn tail to run only to find yourself face to face with the Captain!")
                print("The dark beard and burning cinders remind you of a demon from the pits as he bellows with laughter!")
                print("You fall to your knees and plead for you life, but he lops off your head in a single swing.")

            elif q4 == "wait":
                print("You bide your time and wait behind a pillar. Not long after you hear laughter and whispers.")
                print("The Captain and crew come with more loot to bury. Your eyes fixated on the chest, but you notice the captain hit a switch on the other pillar")
                print("A cage drops and you notice tentacles writhe about in pain. After dropping of the loot the button is again pressed and the crew departs")
                print("Pressing the button you fill your satchel and head out getting away with the Pirate's Booty!")
                print("Congrats on winning the game!!!")

elif quest == "right":
    print("As you make you way down the tunnel on your right you feel the sands shift and the ground gives way\nThe last thing you see before nothingness is the spikes below...")

else:
    print("That is not a valid option...")