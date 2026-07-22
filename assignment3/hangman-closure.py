def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        if letter not in guesses:
            guesses.append(letter)

        display_word = ""
        all_guessed = True

        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += '_'
                all_guessed = False

        print(f'Current word: {display_word}')

        return all_guessed
    
    return hangman_closure

if __name__ == '__main__':
    print('---Welcome to Hangman (Closure Edition) ---')
    secret = input('Enter the secret word for your player: ').strip().lower()

    game = make_hangman(secret)

    solved = False
    while not solved:
        guess_letter = input('Guess a letter: ').strip().lower()
        if len(guess_letter) > 0:
            solved = game(guess_letter[0])
            if solved:
                print('Congratulations, you guessed the entire word!')