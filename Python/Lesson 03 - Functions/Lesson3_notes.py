#Problem 1
# for number in range(0,101):
#     if number % 3 == 0 and number % 3 == 0:
#         print ("FizzBuzz")
#     elif number % 3 == 0:
#         print ("Fizz")
#     elif number % 5 == 0:
#         print ("Buzz")
#     else:
#         print(number)

#Problem 2
# user_input = input("Choose rock, paper, or scissors: ")
# computer_input = "rock"

# if user_input== "rock" and computer_input == "rock" :
#     print ("You tie")
# elif user_input== "rock" and computer_input == "paper" :
#     print ("You lose")
# elif user_input== "rock" and computer_input == "scissors" :
#     print ("You win")
# elif user_input== "paper" and computer_input == "rock" :
#     print ("You win")
# elif user_input== "paper" and computer_input == "paper" :
#     print ("you tie")    
# elif user_input== "paper" and computer_input == "scissors" :
#     print ("You lose")
# elif user_input== "scissors" and computer_input == "rock" :
#     print ("You lose")
# elif user_input== "scissors" and computer_input == "paper" :
#     print ("you win")    
# elif user_input== "scissors" and computer_input == "scissors" :
#     print ("You tie")  


# #Problem 3 
# import random 
# random_number = random.randrange(1,100)

# user_number = int(input("Enter a number between 1 and 100"))
# count = 1
# num_guesses = 0
# while user_number != random_number:
#     if user_number > random_number:
#         (print(" You Guessed too high!"))
#     else:
#         print("You Guessed too low")
#     user_number = int(input("Enter a number beteen 1 and 100: "))
#     count += 1
#     num_guesses =+ 1

# if num_guesses <5:
#     print(f"Congrats, you guessed {random_number} in {num_guesses} tries")
# else:
#     print ("better luck next time!")

#Problem 4
# import random
# random_int = random.randint(0,100)

# if random_int < 50:
#         print("The number is less than 50")
# elif random_int >50: 
#         print ("The number is greater than 50")
# elif random_int == 50:
#         print ("The number is equal to 50")

# def area_function (length, width):
#     return length * width
 
# length = int(input("Choose integer input 1: "))
# width = int(input("Choose integer input 2: "))

# result = area_function(length,width)
# print(result)

# def tip_function (total:float, percent:float)-> float:
#     percent_by_100 = percent /100
#     return total * percent_by_100
 
# total_arg = int(input("what is the total? "))
# percent_arg = int(input("what percent "))

# result = tip_function(total_arg,percent_arg)
# print(f" the total reccomnended amount is {result}")


def has_more_characters (string1: str, string2:str) -> str:
    if len(string1) > len(string2):
        return f"{string1} has more characters"
    elif len(string1)< len(string2):
        return f"{string2} has more characters"
    else:
        return f"{string1} and {string2} are equal"
    
string1_arg = str(input("what is the the frst string? "))
string2_arg = str(input("what is the the second string? "))

result = has_more_characters(string1_arg,string2_arg)
print(result)