import sys
from Juego import Juego

def main():
    
    juego = Juego(sys.argv[1:])
    return juego.iniciar_juego()



if __name__ == "__main__":
    main()