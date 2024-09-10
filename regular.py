

def regular_falsi(f, a, b):
    def fun(x):
        fun = eval(f)
        return fun
    if(fun(a)*fun(b) >= 0):
        print("Invalid guess")
        return
    c = a
    while((b - a) >= 0.01):
        c = (a*fun(b)-(b*fun(a)))/(fun(b)-fun(a))
        if(fun(c) == 0.0):
            break
        if(fun(a)*fun(c) < 0):
            b = c
        else:
            a = c
    print("The value of root is: %.4f" % c)


fun = input("Enter your equation: ")
a = int(input("Enter first value:"))
b = int(input("Enter second value:"))


regular_falsi(fun, a, b)
