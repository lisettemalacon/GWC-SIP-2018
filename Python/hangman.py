# Have a word/phrase
phrase = "girls who code"

# Keep track of user's guesses
guessed_letters = []
game_over = False
# Tell user how many spaces and letters they need to guess
display = ""
for letter in phrase:
    if letter in guessed_letters:
        display += letter
    elif letter == " ":
        display += "  "
    # the letter in our phrase has not been guessed yet
    else:
        display += "_ "
print(display)

while game_over != True:
# Allow user to give input to computer
    guess = input("Enter a letter: ")

    # Tell the user if they get the right letter
    if guess in phrase:
        print("You got a letter: {}".format(guess))
    else:
        print("{} is not in the phrase.".format(guess))
    #Add the guess letter to our list or guessed letters
    guessed_letters.append(guess)

    # Tell user how many spaces and letters they need to guess
    display = ""
    for letter in phrase:
        if letter in guessed_letters:
            display += letter
        elif letter == " ":
            display += "  "
        # the letter in our phrase has not been guessed yet
        else:
            display += "_ "
    print(display)

    # game_over = True
    total_underscores = 0
    for d in display:
    # There is still an underscore aka not all letters have been guessed
        if d == "_":
            total_underscores += 1
    if total_underscores == 0:
        game_over = True
    else:
        game_over = False

print("END OF GAME")
            # game_over = False

# End the game if the user gets all the right letters in our word/phrase
