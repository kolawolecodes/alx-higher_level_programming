#!/user/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = -(abs(number) % 10) if (number < 0) else number % 10
string = f"Last digit of {number:d} is {last_digit}"
if last_digit > 5:
    print(f"{string} is greater than 5")
elif last_digit == 0:
    print(f"{string} is 0")
elif (last_digit < 6) & (last_digit != 0): 
    print(f"{string} is less than 6 and not 0")
