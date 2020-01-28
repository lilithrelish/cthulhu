import time

from time import sleep

import os

if os.name == "posix":
    var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
os.system(var)

i = True
action = ''
go_to = ''
option = ''
take_object = ''
travel_to = ''
name = ''
surname = ''
profession = ''
treat = ''
inventory = ['', '', '']
optionInventory = ''
level = 4



def Introduction():
    print("London, 21 august, 1939")
    print("9 AM")
    time.sleep(2)
    print("You are in your house, peacefully...")
    time.sleep(2)
    print("All of sudden, the bell rings... There's someone at the entrance?")
    time.sleep(2)


def HouseHall():
    os.system(var)
    print("You enter in the hall. It's a big space where the walls are decorated with portraits of people that you've never met")
    time.sleep(2)
    print("At the left side of the principal door, there's an umbrella stand with three umbrellas.")
    time.sleep(2)
    print("At the right side, there's a big mahogany wardrobe with the doors closed.")


def HouseDinningRoom():
    os.system(var)
    print("You enter in the dinning room. It's a big room with an oak desk in the middle,")
    print("it looks like more than ten people could easily fit for a formal dinner...")
    time.sleep(2)
    print("The walls are beautifully decorated with an intrincate design paper")
    time.sleep(2)
    print("And a delicate chandelier hangs from the ceiling like a crystal cascade...")


def HouseBedroom():
    os.system(var)
    print("You enter in the bedroom. There's a canopy bed againts the right wall, and a wardrobe in front")
    time.sleep(2)
    print("A window let the gray light enter in the room...")


def HouseStudio():
    os.system(var)
    print("You enter in the studio. Everything remains in order, ")

def Inventory():
    os.system(var)


while i == True:
    while level < 0:
        Introduction()
        print("Where do you want to go? Please, write your actions in the same way that are writed, without the number...")
        time.sleep(1)
        print("1. Dinning Room")
        time.sleep(1)
        print("2. Entrance Hall")
        time.sleep(1)
        print("3. Bedroom")
        time.sleep(1)
        print("4. Studio")
        time.sleep(1)
        go_to = input()
        time.sleep(5)

        if go_to == "Dinning Room":
            HouseDinningRoom()
            
        if go_to == "Bedroom":
            HouseBedroom()
            
        if go_to == "Studio":
            HouseStudio()
            

        if go_to == "Entrance Hall":
            HouseHall()
            print("What do you want to do?")
            time.sleep(1)
            print("1. Look in the wardrobe")
            time.sleep(1)
            print("2. Take an umbrella")
            time.sleep(1)
            print("3. Open the door")
            time.sleep(1)
            action = input()
            time.sleep(2)

            if option == "Look in the wardrobe":
                os.system(var)
                if name == '':
                    print("???: Oh, it's closed...")
                else:
                    print(name, ": Oh, it's closed...")
            if option == "Take an umbrella":
                if name == '':
                    print("???: Well, maybe I'll need this later...")
                    print("You take an umbrella and store it in the inventory...")
                else:
                    print(name, ": Well, maybe I'll need this later...")
                    print("You take an umbrella and store it in the inventory...")
            if option == 'Open the door':
                level = level - 1
                os.system(var)
                print("You open the door. Cold air enters in your house and gives you chills")
                time.sleep(1)
                print("A mailman waits at the end of the stairs of the porch, and when he sees you, he salutes you with his hat")
                time.sleep(1)
                print("Good morning...")
                print("Sir or Madam?")
                treat = input()
                print("Good morning", treat, "I have a letter for...")
                print("What's your name?")
                name = input()
                print("And your surname?")
                surname = input()
                print("Yes, for", name, "er...", surname)
                time.sleep(2)
                print(name, ": Oh, for me?")
                time.sleep(2)
                print("Mailman: Yes", treat, "I have it here...")
                time.sleep(2)
                print("The mailman searchs inside his bag and then gives you a letter that you take...")
                time.sleep(2)
                print("Mailman: Have a good day", treat)
                time.sleep(2)
                print("The mailman leaves, and you close the door")
                time.sleep(2)
                print("What do you want to do?")
                print("1. Go to another room (write the name of the room)")
                time.sleep(1)
                print("2. Open the letter")
                time.sleep(1)
                option = input()
                if option == 'Open the letter':
                    print(name,": Mmm, I think that I need something to open this...")
                    time.sleep(1)
                    print(name,": there are a letter opener in my studio...")
                    time.sleep(1)
                if option == "Go to another room":
                    print("Where do you want to go?:")
                    go_to = input()
                    i = False
