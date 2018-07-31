# --- Define your functions below! ---
def intro():
    print("Howdy! Welcome to Chatbot.")

def greeting():
    print("Let's get to know each other ;)")

def dating():
    print("I am Chatbot. I like to eat cereal.")
    print("During the day, I am a cereal killer. At night, I write poetry for my lovers.")
    rep = input("Sooooo, come here often? ")
    poet()

def goodbye():
    bai = input("Say 'bye to end the chat'")
    if bai == "bye":
        print("pupinia chan wa kawaii koneko desu ne WAFU!!! (◠‿◠✿)(>.<) anata no koto ga daisuki desu ＼(*^▽^*)/ shimeru desu ka? ｡◕ ‿ ◕｡<3 watashi wa weeaboo janai gaijin otaku desu. watashi ni tsukiatte kudasai!! (`･ω･´)okane ga arimasu yo :3 ")


def poet():
    poem = input("Want to hear a poem? ")
    if poem == "yes":
        print("Roses are red,\n Violets are blue,\nPlease invite me to kill cereal with you ;)")
        goodbye()
    else:
        print(""".----------------.   .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .--
| .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. |
| |     _____    | | | |  ____  ____  | || |      __      | || |  _________   | || |  _________   | | | |  ____  ____  | || |     ____     | || | _____  _____ | |
| |    |_   _|   | | | | |_   ||   _| | || |     /  \     | || | |  _   _  |  | || | |_   ___  |  | | | | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| |
| |      | |     | | | |   | |__| |   | || |    / /\ \    | || | |_/ | | \_|  | || |   | |_  \_|  | | | |   \ \  / /   | || |  /  .--.  \  | || |  | |    |   | |
| |      | |     | | | |   |  __  |   | || |   / ____ \   | || |     | |      | || |   |  _|  _   | | | |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | |
| |     _| |_    | | | |  _| |  | |_  | || | _/ /    \ \_ | || |    _| |_     | || |  _| |___/ |  | | | |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | |
| |    |_____|   | | | | |____||____| | || ||____|  |____|| || |   |_____|    | || | |_________|  | | | |   |______|   | || |   `.____.'   | || |    `.__.'    | |
| |              | | | |              | || |              | || |              | || |              | | | |              | || |              | || |              | |
| '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' |
 '----------------'   '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------' """)

def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False


# --- Put your main program below! ---
def main():
    valid_input = ["Hi", "te amo", "okay ;)", ";/", "yes"]
    intro()

    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input):
            if answer == "Hi":
                greeting()
            elif answer in ["okay ;)", "te amo", ";/"]:
                dating()
        else:
            print("These are the inputs I understand: ")
            for vi in valid_input:
                print(vi)
            print("...I don't understand anything else.")



# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
  main()
