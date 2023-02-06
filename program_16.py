# Generate a random integer from a to b. You and your friend have to guess a number between two numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number, and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game, and then the person with the minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.
'''Input:
Enter the value of a
4
Enter the value of b
13
Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again
8
Wrong guess a smaller number again
6
Correct, you took 3 trials to guess the number
Player 2:
Correct, you took 7 trials to guess the number
Player 1 wins!'''

import random

def guess_Game(a, b, actual):
    guess_number = int(input(f"Guess a number between {a} and {b}: "))
    n_guess = 1
    while n_guess != actual:
        if guess_number< actual:
            guess_number = int(input(f"Enter a bigger number: "))
            n_guess += 1
        else: 
            guess_number = int(input(f"Enter a smaller number: "))   
            n_guess += 1

    print(f"You guessed the number in {n_guess} guesses: ")
    return n_guess


if __name__ == "__main__":
    a = int(input("Enter the value of a: "))    
    b = int(input("Enter the value of b: "))
    actual_1 = random.randint(a, b)  
    print("Player 1's turn\n")
    g1 = guess_Game(a, b, actual_1)
    print("Player 2's turn\n")
    actual_2 = random.randint(a, b)  
    g2 = guess_Game(a, b, actual_2)

    if g1 < g2:
        print("Player 1 won the match!: ")

    elif g1 > g2:
        print("Player 2 won the match!: ")    
    
    else:
        print("Its a Tie!: ")
    
    print(f"The number for player 1 was {actual_1} and for player 2 was {actual_2}")
    
