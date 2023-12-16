# -----liberis----------------
import random

# ----------openingTexture-------------------------------------------
def openingTexture():
    HANGMAN_ASCII_ART = (r"""Welcome to the game Hangman
        _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \  
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                        |___/
    """)
    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)
    return None

# -------inputWord---------------------------------------------
def inputWord(secret_word):
    print ("_ " * len(secret_word))
    return None

# -------inputLetter---------------------------------------------
def inputLetter():
    return input("Guess a letter: ")

# -------is_valid_input---------------------------------------------
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    function who check if the parram is correct
    :param letter: need to be one alphabit letter.
    :type letter: string
    :return: true or false.
    :treturn: bool
    """
    if ((len(letter_guessed) > 1) or
        (not letter_guessed.isalpha()) or
        (letter_guessed in old_letters_guessed)):
        return False
    return True
# -----------------check_valid_input------------------------------------------
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    old_letters_guessed.sort()
    if(not (check_valid_input(letter_guessed, old_letters_guessed))):
        print("x", "\n", "-> ".join(old_letters_guessed), "\n", False)
        return False
    else:
        old_letters_guessed += [letter_guessed]
        return True
# --------show_hidden_word----------------------------------------
def show_hidden_word(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter in old_letters_guessed:
            print(letter," ", end = '')#print without new line
        else:
            print("_ ", end = '')#print without new line
    return
# --------main----------------------------------------
def main():
    # lists
    letter_guessed =""
    secret_word = "mammals"
    old_letters_guessed = []

    openingTexture()
    inputWord(secret_word)
    letter_guessed = inputLetter()

    try_update_letter_guessed(letter_guessed, old_letters_guessed)
    show_hidden_word(secret_word, old_letters_guessed)


if __name__ == "__main__":
    main()