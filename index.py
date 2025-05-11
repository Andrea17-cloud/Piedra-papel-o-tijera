import sys
from game import Play

def main():
    
    game = Play(sys.argv[1:])
    return game.startGame()



if __name__ == "__main__":
    main()