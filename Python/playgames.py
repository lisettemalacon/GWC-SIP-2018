# TODO: import your games library into this folder
import games

#TODO: create a list of available games
available_games = ["Even or odd", "Riddle"]
#TODO: create a function to display the list of available available games
    #HINT: use a loop
def display_games():
    for g in available_games:
        print(g)

#TODO: write a function to evaluate the player's choice of game
def evaluate_choice():
    player_choice = input("What game would you like to play? ")
    if player_choice == "Even or odd":
        games.evenorodd()
    if player_choice == "Riddle":
        games.riddle()

    #TODO: ask the player which game they wish to play
    #TODO: run that particular game by calling the respective game with the dot notation

#TODO: define a main function to run the games
def main():
    repeat = True
    while repeat: #variable here
    #TODO: call the # that displays a list of available available_games
        display_games()
        #TODO: call the function that evaluates the player's choice of game
        evaluate_choice()
        #TODO: ask the player if they wish to keep playing
        play_again = input("Do you wish to play again (Y/N)?")
        #TODO: use a loop to keep playing if the player answers yes
        if play_again == "Y":
            repeat = True
            #playagain
        else:
            repeat = False
        #stop

#TODO: call the main function appropriately

if __name__ == "__main__":
    main()
