from GUI.window import GameBoard

def main():
    plot_game = True

    game_class = GameBoard()
    if plot_game:
        game_class.mainloop()



if __name__ == '__main__':
    main()