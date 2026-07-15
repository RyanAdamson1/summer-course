# Exercise Conditional staements
#Write a script that asks a user for a number.  The script then checks the number and prints “positive,” “zero,” or “negative”

#usernum = float(input("pick a number:  "))
#Exercise 1

# if usernum > 0:
#     print ("Positive")
# elif usernum < 0:
#     print ("negative")

# elif usernum == 0:
#     print ("The number is 0")

#Exercise 2: Even or odd
# if usernum == 0:
#     print(f"{usernum} is even ")

# elif (usernum % 2):
#     if usernum == 0:
#         print(f"{usernum} is even ")
#     elif usernum == 1:
#         print(f"{usernum} is odd ")

# # Exercise 3 
# userage = float(input("What is your age?  "))
# if userage <= 13:
#     print ("Under 13")
# elif userage <6013:
#     print ("Teenager")
# elif userage <20:
#     print ("Adult")
# elif userage <65:
#     print ("Senior")



#Exercise 1 
#  user_num= int(input ("Choose an even integer number: "))

# while user_num % 2 == 1:
#     user_num = int(input("This is an odd number choose again:  "))


# print (f"good job youre not stupid, {user_num}")

#Exercise 2 
secret_number = 44
user_guess = int(input("Guess an integer number: "))
count = 0

while user_guess != secret_number:
    if user_guess < secret_number:
        print( "too low!")
    else:
        print ("Too high!")
    user_guess = int(input("Guess an integer number: "))
    count += 1
    print (f"Congratulations, you guessed the corect number {user_guess}")
    print (f"it took you {count} number of guesses to complete this")