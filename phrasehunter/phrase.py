# Create your Phrase class logic here.
class Phrase:
    # universal class attributes

    def __init__(self, phrase):  # Instance of phrase class that will be used in program.
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:  # Fills in guessed letters in phrase.
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_ ", end=" ")  # Fills in unguessed letters with underscores.

    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):  # Checks if every letter in phrase is present in guesses list.
        check = None
        for letter in self.phrase:
            if letter in guesses:
                check = True
            else:
                check = False
                break
        return check

    def __str__(self):  # Allows phrase to be returned as a string.
        return f"{self.phrase}"
