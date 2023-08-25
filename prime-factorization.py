a = int(input("Enter a natural number: "))
number = a

i = 2
factors = []
while i <= a ** 0.5:
    d = a % i
    if d == 0:
        factors.append(str(i))
        a //= i
    else:
        i += 1
factors.append(str(a))

result = " · ".join(factors)
print(result)
