# This algorithm generates a list of user's integer input divisors

divisors = []

a = int(input("Enter a natural number: "))
print()

i = 1
while i <= a ** 0.5:
    d = a % i
    if d == 0:
        divisors.append(i)
    i += 1

divisors1 = []
j = 0
for k in divisors:
    divisors1.insert(0, a // k)

if divisors[-1] != divisors1[0]:
    divisors.extend(divisors1)
else:
    divisors1.pop(0)
    divisors.extend(divisors1)

print(divisors)
print()
print("(!) Dividers amount:", len(divisors))
