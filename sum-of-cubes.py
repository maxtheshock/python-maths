# This algorithm defines whether user's integer input is representable as a sum of 2 cubes
# or not. If number is representable, it finds all the combinations

import math

a = int(input("Enter a natural number: "))
print()

n1 = 1
counter = 0
isRepresentable = None

while n1 <= round(((4 * a) ** (1/3)) * 0.5) and a - (n1 ** 3) > 0:
    n2 = (a - (n1 ** 3)) ** (1/3)
    n3 = round(n2)
    if n1 ** 3 + n3 ** 3 == a and n3 >= n1:
        print("[!] Result found: ", n3, "³ + ", n1, "³ = ", a, sep="")
        n1 += 1
        counter += 1
        isRepresentable = True
    else:
        n1 += 1

if isRepresentable != True:
    print("[!] The number has no representation as a sum of 2 cubes")
elif isRepresentable == True and counter > 1:
    print()
    print("(!) Combinations:", counter)