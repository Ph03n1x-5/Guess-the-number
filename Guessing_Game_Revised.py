import random

random.seed()   #Prepare random number generator

print("Do you wish to play the [Guess the number game]? [Type 'y' or 'Y' for yes otherwise type no to Exit the program]")
answer = input()
while answer == "y" or answer == "Y":
    number = int(random.random() * 101)
    
    # Output statement to provide directions to user
    print("Guess a magic number between 0 and 100")
    
    # guess will be initially set to -1
    guess = -1
    
    # attempt will be initially set to 0
    attempt = 0
    
    # While Loop to prompt the user to enter numbers continuously until it matches the randomly generated number
    while guess != number:
        
        # prompt user to guess the number
        print("Enter your guess [positive whole values only]")
        guess = int(input())
        
        # keeps count of the number of attempts to guess the number
        attempt = attempt + 1
        
        # nested if to analyze guessed value entered by user
        if guess == number:
            print("You guessed the correct number ==> " + format(guess) + " in " + format(attempt) + " attempts")
        else:
            if guess > number:
                print("Your guess of " + format(guess) + " is too high")
            else:
                print("Your guess of " + format(guess) + " is too low")
        
        # end while loop
    # IF statement to determine if user wins or loses the game
    if attempt <= 4:
        print("You are a winner, guessing the correct number ==> " + format(guess) + " in " + format(attempt) + " tries / attempts")
    else:
        print("To obtain a winning status, you need to play the game again!!")
    print("Do you wish to play the [Guess the number game Again]? [Type 'y' or 'Y' for yes otherwise type no to Exit the program]")
    answer = input()

# end while loop
print("THANKS FOR PLAYING THE GUESS THE NUMBER GAME - HAVE A NICE DAY!")

# END PROGRAM
