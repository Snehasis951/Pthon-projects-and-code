import random
lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
number = "0123456789"
symbol = "[]{}()!@#$%^&*_-+<>,./?\|`~"

all = lower + upper + symbol + number
length = 9
password = "".join(random.sample(all, length))
print("The new generated password is : ", password)