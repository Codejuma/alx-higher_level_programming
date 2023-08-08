#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            a = "FizzBuzz"
        elif a % 5 == 0:
            a = "Buzz"
        elif a % 3 == 0:
            a = "Fizz"
        print("{}".format(a), end=' ')
