
def game(computer_choice, user_choice):
    
    if user_choice == "rock" and computer_choice == "paper":
        return("You Lose")
    elif user_choice == "rock" and computer_choice == "scissors":
        return("You Win")
    elif user_choice == "paper" and computer_choice == "scissors":
        return("You Lose")
    elif user_choice == "paper" and computer_choice == "rock":
        return("You Win")
    elif user_choice == "scissors" and computer_choice == "rock":
        return("You Lose")
    elif user_choice == "scissors" and computer_choice == "paper":
        return("You Win")
    else:
        return("You tie")

games_list = [1,3,5,7,9]
while True:
    user_input = int(input(f"\nChoose an odd number between 1-9 for how many games you would like to play. \ngames will be best of the chosen number: "))

    if user_input == games_list:
        print (f"\nyou have chosen {user_input} amount of games\n")
    else:
        print (f"\n you have chosen a wrong number, try again")
        