# This algorithm figures out whether number is prime or not

import time

a = int(input("Enter a natural number: "))
print()
i = 2

start_time = time.time()
while i <= a ** 0.5:
    d = a % i
    if d == 0:
        break
    else:
        i += 1
end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time *= 1000
el_time = elapsed_time

if elapsed_time < 1000:
    ms = int(elapsed_time // 1)
    elapsed_time = str(ms) + " ms"
elif 1000 <= elapsed_time < 60000:
    secs = int(elapsed_time // 1000)
    ms = int(elapsed_time // 1 - 1000 * secs)
    elapsed_time = str(secs) + " s " + str(ms) + " ms"
elif 60000 <= elapsed_time < 3600000:
    mins = int(elapsed_time // 60000)
    secs = int((int(elapsed_time // 1) - 60000 * mins) // 1000)
    ms = int(((int(elapsed_time // 1) - 60000 * mins) - 1000 * secs) // 1)
    elapsed_time = str(mins) + " m " + str(secs) + " s " + str(ms) + " ms"

d = a % i
if a == 1:
    print("[!] Num 1 is neither prime nor composite")
elif d != 0 or a <= 3:
    print("[!] Number", a, "is prime")
else:
    print("[!] Number", a, "is not prime")

if int(el_time // 1) != 0:
    print("(!) Elapsed time:", elapsed_time)
