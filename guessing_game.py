# Guessing game

guess_number = 5

# input_guess = None is used to make sure program can initialise the loop. You could use 0, but since 0 is an INT, None works better in that case to not interfer with other values.
input_guess = None

while input_guess != guess_number:
    input_guess = int(input("Whats your guess (Choose from 0 to 10)? "))

    if input_guess > guess_number:
        print("Too high")
    elif input_guess < guess_number:
        print("Too low")
    else:
        print("Correct!")        
