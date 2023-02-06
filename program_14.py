'''A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616, mom, 100001.
You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.
Input:
3
451
10
2133
Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2133 is 2222'''

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n
def is_palindrome(n):
    return str(n) == str(n)[:: -1]

if __name__ == "__main__":
    n = int(input("Enter the number of test cases: "))
    number_list = []
    for i in range(n):
        number = int(input("Enter the number: "))
        number_list.append(number)
    for i in range(n):
        print(f"Next palindrome for {number_list[i]} is {next_palindrome(number_list[i])}")
