# You are given a list that contains some numbers. You have to print a list of the next palindromes only if the number is greater than 10; otherwise, you will print that number.
# Input:
# [1, 6, 87, 43]

# Output:
# [1, 6, 88, 44]

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n
def is_palindrome(n):
    return str(n) == str(n)[:: -1]

if __name__ == "__main__":
    n = int(input("Enter the size of your list: "))
    number_list = []
    for i in range(n):
        number = int(input("Enter the number of the list: "))
        number_list.append(number)
    print(f"You have enter {number_list}")
    print(f"Final list: {[number_list[i] if number_list[i] < 10 else next_palindrome(number_list[i]) for i in range(n)]}")