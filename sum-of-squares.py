# This algorithm defines whether user's integer input is representable as a sum of 2 squares
# or not. If number is representable, it finds all the combinations

import math

a = int(input("Enter a natural number: "))
print()

n1 = 1
counter = 0
isRepresentable = None

while n1 <= ((2 * a) ** 0.5) * 0.5:
    n2 = (a - n1 ** 2) ** 0.5
    n3 = math.floor(n2)
    if n2 == n3 and n1 ** 2 + n3 ** 2 == a:
        print("[!] Result found: ", n3, "² + ", n1, "² = ", a, sep="")
        n1 += 1
        counter += 1
        isRepresentable = True
    else:
        n1 += 1

if isRepresentable != True:
    print("[!] The number has no representation as a sum of 2 squares")
elif isRepresentable == True and counter > 1:
    print()
    print("(!) Combinations:", counter)
