# The task you have to perform is “Your Age In 2090”.
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sorts of errors like :            (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

Age_of_user = int(input("What is your Age/Year of birth\n"))
what_is_age = False
what_is_year = False

if len(str(Age_of_user)) == 4:
    what_is_year = True

else:
    what_is_age = True

if(Age_of_user<1900 and what_is_year):
    print("You seem to be the oldest person alive")
    exit()

if(Age_of_user>2019):
    print("You are not yet born")
    exit()

if what_is_age:
    Age_of_user = 2022 - Age_of_user 

print(f"You will be 100 years old in {Age_of_user + 100}")

Interested_year = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {Interested_year - Age_of_user} years old in {Interested_year}")


 
 