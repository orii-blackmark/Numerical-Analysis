

def secant(fun, x1, x2, E):
    def f(x):
        f = eval(fun)
        return f
    n = 0
    xm = 0
    x3 = 0
    c = 0

    if (f(x1) * f(x2) < 0):
        while True:
            x3 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
            c = f(x1) * f(x3)
            x1 = x2
            x2 = x3

            n += 1
            if (c == 0):
                break
            xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))

            if(abs(xm - x3) < E):
                break

        print("Root of the given equation =", round(x3, 6))
        print("No. of iterations = ", n)

    else:
        print("Can not find a root in ", "the given interval")


fun = input("Enter your equation: ")
x1 = int(input("Enter value of x1:"))
x2 = int(input("Enter value of x2:"))
e = float(input("Enter error: "))
secant(fun, x1, x2, e)
