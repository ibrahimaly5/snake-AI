from GUI.window import GameBoard
import random

def main():
    plot_game = True

    game_class = GameBoard()
    if plot_game:
        game_class.run_game()



if __name__ == '__main__':
    main()