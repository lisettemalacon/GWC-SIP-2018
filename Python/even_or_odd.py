import random

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
evenorodd()
