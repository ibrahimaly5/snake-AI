from GUI.window import GameBoard
import random
from time import sleep

def main():
    plot_game = True

    game_class = GameBoard()
    if plot_game:
        game_class.run_game()



if __name__ == '__main__':
    while True:
        main()
        sleep(5)