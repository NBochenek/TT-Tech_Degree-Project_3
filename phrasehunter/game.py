# Create your Game class logic in here.
import random
from phrasehunter.phrase import Phrase


class Game:
    # Universal attributes here.

    def __init__(self):  # *** Why should I set these attributes in the instance instead of the universal? ***
        self.missed = 0  # Tracks number of misses by player.
        self.phrases = [Phrase("Nothing"),
                        Phrase("We learn"),
                        Phrase("Truth"),
                        Phrase("When liberty"),
                        Phrase("An idea")]
        # self.phrases = [Phrase("Nothing great in the world was accomplished without passion"),
        #                 Phrase("We learn from history that we do not learn from history"),
        #                 Phrase("Truth is found neither in the thesis nor the antithesis"),
        #                 Phrase("When liberty is mentioned we must always be careful to observe whether it is not "
        #                        "really the assertion of private interests which is thereby designated"),
        #                 Phrase("An idea is always a generalization and generalization is a property of thinking")]
        # List of phrase objects.
        # Quotes taken from Goodreads.
        self.active_phrase = self.get_random_phrase()  # Phrase to be used in current round of play.
        self.guesses = [" "]  # List of all guesses made by user.

    def get_random_phrase(self):
        random_num = random.randrange(0, 5)
        random_phrase = self.phrases[random_num]
        self.active_phrase = random_phrase
        return self.active_phrase

    def welcome(self):
        return print("\nWelcome to the phrasehunter game!\n"
                     "\nPresented by G.W.F. Hegel\n")

    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:  # Checks if guesses are
            # left and if all letters in phrase have not been guessed.
            print("Number missed: ", self.missed)
            self.active_phrase.display(self.guesses)  # Displays the phrase with underscores.
            while True:  # Loop that continues until user inputs a letter.
                user_guess = self.get_guess()
                if len(user_guess) > 1:  # Ensures user cannot guess multiple letters at once.
                    print("Invalid Entry. Please enter one letter.")
                    continue
                if user_guess.isalpha() is False:  # Ensures user entry is a letter.
                    print("Invalid Entry. Please enter one letter.")
                    continue
                if user_guess in self.guesses:
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    break

            self.guesses.append(user_guess)  # Adds current guess to the list.
            if not self.active_phrase.check_guess(user_guess):  # If guess is not in the phrase, adds to miss count.
                print("\nBummer. Try Again.\n")
                self.missed += 1
                print(f"You have {5 - self.missed} guesses left.")
        self.game_over()

    def get_guess(self):
        return input("\n\nPlease guess a letter:   ")

    def game_over(self):
        if self.missed == 5:
            print("\nGame over! Please try again.\n")
            print(f"\nThe phrase was: {str(self.active_phrase)}\n")
            self.restart_game()
        else:
            print("\nCongratulations! You won!\n")
            print(f"\nThe phrase was: {str(self.active_phrase)}\n")
            self.restart_game()

    def restart_game(self):
        while True:
            choice = input("Would you like to play again? Y/N:   ").lower()
            if choice == "y":
                self.reset_game()  # Resets
                return self.start()  # Restarts
            if choice == "n":
                print("\nThank you for playing!")
                break
            else:
                print("Invalid entry. Please try again.")
                continue

    def reset_game(self):  # Resets all necessary parameters to start a new game.
        self.missed = 0
        self.active_phrase = self.get_random_phrase()  # Phrase to be used in current round of play.
        self.guesses = [" "]  # List of all guesses made by user.
