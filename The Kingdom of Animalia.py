import Entities as Ent
import time
import os
import pickle
import textwrap
import gameFunctions as game

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
        p1 = Ent.player.player()
        os.system('clear')
        break

    elif viewScreen.lower() == "leaderboard":
        os.system('clear')
        print("\n\n")
        pass

    elif viewScreen.lower() == "load":
        os.system('clear')
        with open('playerData.pkl', 'rb') as playerData:
            p1 = pickle.load(playerData)
        with open('worldData.pkl', 'rb') as worldData:
            currentWorld = pickle.load(worldData)
        with open('questData.pkl', 'rb') as questData:
            questCompletion = pickle.load(questData)
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

"""   Starting the Game   """
os.system('clear')


# Starts player in Midgard
# Sets all quests as uncomplete

if viewScreen.lower() == 'start':
    currentWorld = game.worlds.Midgard()
    questCompletion = [0]


#### Game Loop ####
while True:
    print("You have moved to " + currentWorld.worldName)
    print("Feel free to 'look' around!")
    print("******************" + ("*" * len(currentWorld.worldName)))

# Midgard
    while currentWorld.worldName == "Midgard":
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

            if transferWorld.lower() == 'eden' and p1.level >= game.worlds.Eden.levelGate:
                print(game.worlds.Eden.transferText)
                print("*" * len(game.worlds.Eden.transferText))
                currentWorld = game.worlds.Eden()
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
            print("contemplate why you're still alive")
            print("after thinking something so incredibly stupid")
            time.sleep(2)
            print('\n***************************************************\n')


# Eden
    while currentWorld.worldName == "Eden":
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

            if transferWorld.lower() == 'Midgard' & p1.level >= game.worlds.Midgard.levelGate:
                print(game.worlds.Midgard.transferText)
                print("*" * len(game.worlds.Midgard.transferText))
                currentWorld = game.worlds.Midgard()
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
            time.sleep(2)
            print('\n***************************************************\n')

    while currentWorld.worldName == "Agartha":
        pass
