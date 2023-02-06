# Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!

# Snake water gun

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    user_input = input('Snake,Water,Gun:')
    computer_input = random.choice(lst)

    if user_input == computer_input:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif user_input == "s" and computer_input == "g":
        computer_point = computer_point + 1
        print(f"your guess {user_input} and computer guess is {computer_input} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif user_input == "s" and computer_input == "w":
        human_point = human_point + 1
        print(f"your guess {user_input} and computer guess is {computer_input} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif user_input == "w" and computer_input == "s":
        computer_point = computer_point + 1
        print(f"your guess {user_input} and computer guess is {computer_input} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif user_input == "w" and{computer_input}== "g":
        human_point = human_point + 1
        print(f"your guess {user_input} and computer guess is {computer_input} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif user_input == "g" and{computer_input}== "s":
        human_point = human_point + 1
        print(f"your guess {user_input} and computer guess is {computer_input} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif user_input == "g" and{computer_input}== "w":
        computer_point = computer_point + 1
        print(f"your guess {user_input} and computer guess is {computer_input} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#

  






































