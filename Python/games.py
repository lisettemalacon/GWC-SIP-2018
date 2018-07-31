#TODO: import the random module since you  will need it in your game functions
import random
#: define function even_or_odd
def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this number even or odd?")
    if computer_value%2 == 0 and user_input == "even":
        print("ayy lmao u got it!\n")
    elif computer_value%2 != 0 and user_input == "even":
        print("wronggggg.\n")
    elif computer_value%2 == 0 and user_input == "odd":
            print("wronggggg.\n")
    elif computer_value%2 != 0 and user_input == "odd":
        print("ayy lmao u got it!\n")
    else:
        print("wronggggg.\n")


# define function riddle

def display(riddle, try_number, hint_list):
    print(riddle)
    print(try_number)
    if try_number == 1:
        print("HINT: {}".format(hint_list[0]))
    if try_number == 2:
        print("HINT: {}".format(hint_list[1]))

def riddle():
    guess_count = 0
    riddle = "What do you break before you use it (answer is one word)?"
    answer = "egg" or "Egg"
    hints = ["Breakfast food", "Laid by a chicken"]
    guess = None
    win = False

    for attempt in range(0,3):
        display(riddle, guess_count, hints)
        guess = input("Enter your guess: ").lower().rstrip()
        if answer != guess:
            guess_count += 1
        if answer == guess:
            win = True
            break
    while win != False:
        print("Congrats rarwrr xxDDDD, the answer really be 'egg'! ")
        break
    while win != True:
        break
