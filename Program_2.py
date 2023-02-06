# no of guess 9
# print no of guess 
#game over
#write a program to in order to guess the right number stated by programmer
n = 10
x = 1
print("number of guesses is limited to 5: ")
while(x<=5):
    y = int(input("guess the number: \n"))
    if (y<n):
        print("please enter a greater number: \n")
    elif(y>n):
        print("please enter a smaller number: \n")
    else:
        print("your guess is right")
        print(x, "no of guess has been taken to finish")
        break
    print(5 - x, "no of guess left in hand")
    x = x+1
if(x>5):
    print("game over")