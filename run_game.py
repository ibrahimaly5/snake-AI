from GUI.window import GameBoard

def main():
    plot_game = True

    game_class = GameBoard()
    if plot_game:
        game_class.run_board()



if __name__ == '__main__':
    main()