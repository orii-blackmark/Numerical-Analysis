
import math


def bisection(fun, a, b):
    def func(x):
        func = eval(fun)
        return func
    if(func(a) * func(b) >= 0):
        print("Invalid Guesses")
        return
    c = a
    while((b-a) >= 0.01):
        c = (a+b)/2
        if(func(c) == 0.0):
            break
        if(func(c)*func(a) < 0):
            b = c
        else:
            a = c
    print(f"The value of the root is : %.4f" % c)


print("Enter your equation: ")
equation = input()
print("Enter your first guess value (a): ")
first_value = int(input())
print("Enter your second guess value (b): ")
second_value = int(input())

bisection(equation, first_value, second_value)
