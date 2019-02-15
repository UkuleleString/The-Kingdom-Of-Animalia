import time

class startScreen():
    def __init__(self):
        while True:
            print("********************")
            print("*    Welcome to    *")
            print("*     The Game     *")
            print("*        <3        *")
            print("********************")
            print()
            time.sleep(0.5)
            print("Type 'Start' to start the game")
            print()
            time.sleep(0.5)
            print("Type 'Load' to load the game")
            print()
            time.sleep(0.5)
            print("Type 'Leaderboard' to look at your top scores!")
            print()
            time.sleep(0.5)
            print("Please enter one:")
            viewScreen = (input())
            if viewScreen in ["start", "Start", "START"]:
                self.createPlayer = True
                break
            elif viewScreen in ["Load", "load", "LOAD"]:
                pass
            elif viewScreen in ["Leaderboard", "leaderboard", "LEADERBOARD"]:
                print()
                print()
                pass
            else:
                print("Bitch, this is the fucking title screen. How the fuck you fuckin up already.")
                pass
