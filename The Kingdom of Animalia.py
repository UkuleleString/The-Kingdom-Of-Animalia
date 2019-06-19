from entities.player import player
from entities.items import itemDict
import entities.items as items
from gameFunctions.worlds import worlds
from quests import boxOfQuests
from quests import randQuest
import time
import os
import pickle


os.system('clear')
while True:
    print("********************")
    print("*    Welcome to    *")
    print("*     The Game     *")
    print("*        <3        *")
    print("********************")
    print("\nType 'Start' to start the game")
    print("\nType 'Leaderboard' to look at your top scores!")
    print("\nType 'Load' to load a save game!")
    print("\nPlease enter one: \n")
    viewScreen = input()

    if viewScreen.lower() == "start":
        os.system('clear')
        p1 = player()
        os.system('clear')
        break

    elif viewScreen.lower() == "leaderboard":
        os.system('clear')
        print("\n\n")
        pass

    elif viewScreen.lower() == "load":
        os.system('clear')
        with open("saveGame.pkl", 'rb') as saveGame:
            p1, currentWorld, questCompletion = pickle.load(saveGame)
        print("Welcome back, " + p1.name + "!")
        p1.printStats()
        time.sleep(5)
        break

    else:
        print("""Bitch, this is the fucking title screen.
How the fuck you fuckin up already.""")
        time.sleep(5)
        os.system('clear')
        pass

# Game Worlds


# Starts player in Midgard
# Sets all quests as uncomplete

if viewScreen.lower() == 'start':
    os.system('clear')
    currentWorld = worlds["midgard"]
    questCompletion = [0]


#### Game Loop ####
while True:
    print("You have moved to " + currentWorld["worldName"])
    print("Feel free to 'look' around!")
    print("***************************" +
          ("*" * len(currentWorld["worldName"])))

### Midgard ###
    while currentWorld["worldName"] == "Midgard":
        print("What would you like to do?")
        playerAction = input()
        if playerAction.lower() == "look":
            os.system('clear')
            print("Put info here")
            print("\n*******************************************************\n")
            print("Go to the 'Tavern' to pick up rumors or talk to patrons")
            print("Go to the 'Dungeon' to level up or find items")
            print("Go to the 'Shop' to use your gold to buy equipment")
            print("Use the 'Portal' to go to other worlds")
            print("Use 'save' to save the game")

        elif playerAction.lower() == "tavern":
            os.system('clear')

            pass

        elif playerAction.lower() == "dungeon":
            os.system('clear')
            pass

        elif playerAction.lower() == "shop":
            os.system('clear')
            pass

        elif playerAction.lower() == "portal":
            os.system('clear')
            print('')
            print("Where would you like to go?")
            transferWorld = input()

            if transferWorld.lower() == 'eden' and p1.level >= worlds["eden"]["levelGate"]:
                for i in worlds["eden"]["transferText"]:
                    print(i)
                print("*" * len(worlds["eden"]["transferText"][1]))
                currentWorld = worlds["eden"]
                break

        elif playerAction.lower() == "save":
            os.system('clear')
            with open('saveGame.pkl', 'wb') as saveGame:
                pickle.dump([p1, currentWorld, questCompletion], saveGame)
            print('Game Saved!')

        else:
            os.system('clear')
            print("You kinda just sit there for a while and")
            print("contemplate why you're still alive")
            print("after thinking something so incredibly stupid")
            print('\n***************************************************\n')


### Eden ###
    while currentWorld["worldName"] == "Eden":
        print("What would you like to do?")
        playerAction = input()
        if playerAction.lower() == "look":
            os.system('clear')
            print("Put info here")
            print("\n*******************************************************\n")
            print("Go to the 'Tavern' to pick up rumors or talk to patrons")
            print("Go to the 'Dungeon' to level up or find items")
            print("Go to the 'Shop' to use your gold to buy equipment")
            print("Use the 'Portal' to go to other worlds")
            print("Use 'save' to save the game")

        elif playerAction.lower() == "tavern":
            os.system('clear')
            pass

        elif playerAction.lower() == "dungeon":
            os.system('clear')
            pass

        elif playerAction.lower() == "shop":
            os.system('clear')
            pass

        elif playerAction.lower() == "portal":
            os.system('clear')
            print('')
            print("Where would you like to go?")
            transferWorld = input()

            if transferWorld.lower() == 'midgard' & p1.level >= worlds["midgard"]["levelGate"]:
                print(worlds["midgard"]["transferText"])
                print("*" * len(worlds["midgard"]["transferText"][0]))
                currentWorld = worlds["midgard"]
                break

        elif playerAction.lower() == "save":
            os.system('clear')
            with open('playerData.pkl', 'wb') as playerData:
                pickle.dump(p1, playerData)
            with open('worldData.pkl', 'wb') as worldData:
                pickle.dump(currentWorld, worldData)
            with open('questData.pkl', 'wb') as questData:
                pickle.dump(questCompletion, questData)
            print('Game Saved!')

        else:
            os.system('clear')
            print("You kinda just sit there for a while and")
            print("contemplate why you're still alive after")
            print("thinking something so incredibly stupid")
            print('\n***************************************************\n')


### Agartha ###
while currentWorld.worldName == "Agartha":
    pass
