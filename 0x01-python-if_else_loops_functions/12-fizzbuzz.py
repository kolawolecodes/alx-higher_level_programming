#!/usr/bin/python3
def fizzbuzz():
    var = []
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            var.append("FizzBuzz ")
        elif number % 3:
            var.append("Fizz ")
        elif number % 5:
            var.append("Buzz ")
        else:
            var.append("{:d} ".format(number))
    print("".join(var), end="")
