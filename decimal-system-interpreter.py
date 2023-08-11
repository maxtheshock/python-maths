# This algorithm represents decimal numbers in any other from 2 to 36

a = int(input("Enter a natural number: "))
b = int(input("Choose a number system (from 2 to 36): "))
if b < 2 or b > 36:
    while b < 2 or b > 36:
        b = int(input("[!] You have to choose an integer from 2 to 36! "))
print()

digits = []
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
result = ""
while a > 0:
    digit = a % b
    if 10 <= digit <= 35:
        digit = letters[digit-10]
    digits.append(digit)
    a //= b
digits.reverse()

for digit in digits:
    result = str(result) + str(digit)

print(result)
