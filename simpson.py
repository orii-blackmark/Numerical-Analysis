

def simpson13(fun, x0, xn, n):
    def f(x):
        f = eval(fun)
        return f
    h = (xn-x0)/n
    integration = f(x0)+f(xn)

    for i in range(1, n):
        k = x0+i*h
        if i % 2 == 0:
            integration = integration+2*f(k)
        else:
            integration = integration+4*f(k)

    integration = integration*h/3

    return integration


fun = input("Enter your equation: ")
lower_limit = float(input("Enter lower limit of integration:"))
upper_limit = float(input("Enter upper limit of integration:"))
sub_interval = int(input("Enter number of sub intervals:"))


result = simpson13(fun, lower_limit, upper_limit, sub_interval)
print("Integration result by simpson's 1/3 method is: %0.6f" % (result))
