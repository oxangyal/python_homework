# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        displayed = ''.join(
            c if c in guesses else '_' for c in secret_word
        )
        print(displayed)
        return set(secret_word) <= set(guesses)

    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter the secret word: ")
    hangman_game = make_hangman(secret_word)

    print("\nLet's play Hangman!")
    while True:
        guess = input("Enter a letter: ")
        if not guess or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if hangman_game(guess):
            print("Congratulations! You've guessed the word!")
            break
