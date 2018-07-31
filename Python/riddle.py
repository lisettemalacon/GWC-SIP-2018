
def display(riddle, try_number, hint_list):
    print(riddle)
    print(try_number)
    if try_number == 1:
        print("HINT: {}".format(hint_list[0])) # TODO: Access hint_list for a hints
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
        print("HAAAA YOU WRROOONNGGGGGGGG!! The correct is 'egg'! Gotcha!")
        break

if __name__ == "__main__":
    riddle()

    #       Be sure to include the right answer in your message
    #
    #      i.e. "Congrats! The answer is indeed _____" for winning,
    #      "WRRRROOOOONG. The correct answer is _____" for losing
