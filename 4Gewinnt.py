from MainGame import MainGame

def main() -> None:
    play = True

    while play:
        game = MainGame()
        game.prepare_game()
        game.play()

        while True:
            again = input("Would you like to play again? (y/n)")
            if again == "y":
                play = True
                break
            elif again == "n":
                play = False
                break
            else:
                print("Enter 'y' for yes or 'n' for no.")

if __name__ == '__main__':
    main()
