from math import *

expr = input("Enter a function:\n")

a = float(input("[!] Enter first segment bound: "))
b = float(input("[!] Enter second segment bound: "))

x1 = a
x2 = b
x3 = x2
exact = None

i = 0
while i <= 100:
    f1 = eval(expr.replace("x", "x1"))
    f2 = eval(expr.replace("x", "x2"))
    if (f1 * f2) < 0:
        x3 = x2
        x2 = (x1 + x2) / 2
    elif (f1 * f2) > 0:
        x1 = x2
        x2 = (x2 + x3) / 2
    else:
        print()
        exact = True
        if f1 == 0:
            print("[!] Result:", x1)
        elif f2 == 0:
            print("[!] Result:", x2)
        break
    # print("Iteration #", i, ": ", x2, sep="")
    i += 1

if not exact:
    if f1 < 10 ** (-15):
        print()
        print("[!] Result:", x2)

    else:
        print("[!] Could not find any root")