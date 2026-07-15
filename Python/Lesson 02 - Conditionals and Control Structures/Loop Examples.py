user_num= int(input ("Choose an even integer number: "))

while user_num % 2 == 1:
    user_num = int(input("This is an odd number choose again:  "))


print (f"good job youre not stupid, {user_num}")

user_guess = int(input("Guess an integer number: "))
secret_number = 44

while user_guess != secret_number:
    if user_guess < secret_number:
        print( "too low!")
    else:
        print ("Too high!")
    user_guess = int(input("Guess an integer number: "))
    count += 1
    print (f"Congratualtions, you guessed the corect number {user_guess}")
    print (f"it took you {count} number of guesses to complete this")