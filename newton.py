
def newtonmethod(fun, funderivertive, x, n):
    def f(x):
        f = eval(fun)
        return f

    def df(x):
        df = eval(funderivertive)
        return df

    for itercept in range(x, n):
        i = x - (f(x))/(df(x))
        x = i
    print(f"The root was found to be at %.4f after {n} iterations " % x)


fun = input("Enter your equation: ")

df = input("Enter df of the equation:")
x = int(input("Enter value of x:"))
n = int(input("Enter number of iterations:"))

newtonmethod(fun, df, x, n)
