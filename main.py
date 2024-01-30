from pretty_prints import PrettyPrints
from start_menu import StartMenu
from game import Game
from csv_edit import CSVEditor
from wordle import WordBank



if __name__ == "__main__":
    while True:
        p_print = PrettyPrints()
        word_bank = WordBank()
        s_menu = StartMenu()
        s_menu.loginMenu()
        if s_menu is not None:
            play = ""
            while play != "q":
                game = Game(s_menu.user, word_bank)
                game.playGame()
                if game.victory: 
                    game.user.wins += 1
                    print(p_print.game_over.format("Victory!!",game.word))
                else:
                    game.user.losses += 1
                    print(p_print.game_over.format("Deafeat!!",game.word))
                s_menu.user.addToHighscore(game.score)
                play = input("Press 'a' to add word to file, 'q' to quit or press 'enter' to continue: ").lower()
                if play == "a":
                    word_bank.addToFile()
  
            print(s_menu.user)
            input("\nPress enter to continue")
         
            CSVEditor().updateFile(s_menu.user)
        
