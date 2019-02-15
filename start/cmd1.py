class game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
####################################
####     Program  Functions    #####
####################################
    def something():
        pass


####################################
####    User Usable Commands    ####
####################################

    def do_quit(self, args):
        """Leaves the game """
        print("Thank you for playing!")
        return True
        exit()

    def do_move(self, *args, **kwargs):
        """Progresses to the next room"""
        pass

if __name__ == "__main__":
    game = game()
    game.cmdloop()
