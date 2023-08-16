import math

a = float(input("[!] Введите начало отрезка: "))
b = float(input("[!] Введите конец отрезка: "))

x1 = a
x2 = b
exact = None

i = 0
while i <= 60:
    f1 = x1 ** 3 - 4 * (x1 ** 2) + x1 + 1
    f2 = x2 ** 3 - 4 * (x2 ** 2) + x2 + 1
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
    print("Iteration #", i, ": ", x2, sep="")
    i += 1

if not exact:
    print()
    print("[!] Result:", x2)