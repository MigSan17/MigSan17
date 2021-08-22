from sys import exit

def gold_room():
    print("\n ----- GOLD ROOM ----- \n")
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    try:
        how_much = int(choice)
    except:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("\n ----- BEAR ROOM ----- \n")
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while  True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off..")
        elif choice == "open door" and bear_moved:
            abyss_room()
        else:
            print("I got no idea what that means.")

def abyss_room():
    print("\n ----- ABYSS ROOM ----- \n")
    print("Got ya bitch. \nWelcome to you're demise. \nYou cannot escape as an unknown force is pulling you")

    choice = input("> ")
    if choice == "enter":
        dead("End of the line.")
    else:
        dead("Thought you could runaway? Wrong.")

def blackjack_room():
    print("\n ----- BLACKJACK ROOM ----- \n")
    print("Upon going through the door, you see skeletons playing blackjack.")
    print("They invite you into a hand.")
    print('You get dealed a hand of 19.')
    print('Do you hit or stay?')

    choice = input("> ")

    if choice == "hit":
        dead("You went over 21 and the skeleton beside you stabbed you \n")
    if choice == "stay":
        print("You have the highest hand and let you through another door. \n")
        cup_room()

def cup_room():
    print("\n ----- CUP ROOM ----- \n")
    print("An elderly man greets you and points at 5 cups.")
    print("He states that you must drink one.")
    print("Pick right, you are transported to the gold room.")
    print("Which cup to you drink from?")

    choice = input("> ")
    cup = int(choice)

    if cup == 3:
        gold_room()
    elif cup != 3:
        dead("Wrong choice, idiot!")

def spider_room():
    print("\n ----- SPIDER ROOM ----- \n")
    print("Boom! A huge mother spider catches you.")
    print("It is blocking your way to a door.")
    print("The spider looking at you starts to wind up it's web.")
    print("Do you fight the spider or hide in the closet near you?")
    spider_wall = False

    while True:
        choice = input("> ")

        if choice == "hide":
            dead("You acted like a pussy and the spider took advantage of it!")
        if choice == "fight" and not spider_wall:
            print("The spider is caught off-guard and webs up at the ceiling.")
            print("You can now walk through the door.")
            spider_wall = True
        elif choice == "kill spider" and spider_wall:
            dead("The spider becomes agitated and webs you up.")
        elif choice == "walk through door" and spider_wall:
            blackjack_room()

def cthulhu_room():
    print("\n ----- CTHULHU ROOM ----- \n")
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "You suck!")
    exit(0)

def start():
    print("\n ----- START ----- \n")
    print("You are in a dark room.")
    print("THere is a door to your right and left and in front.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "in front":
        spider_room()
    else:
        dead("You stumble around the room until you starve.")

start()
