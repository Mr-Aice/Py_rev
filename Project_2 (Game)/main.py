from Game import Game, Player




def main():
    p1 = Player(fname="Muhammad", lname="Awais")

    g1 = Game(p1)

    print(g1.state)
    print(g1)
    g1.attack()




main()

