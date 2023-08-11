# This method finds the closest prime numbers to user's input

import time

a = int(input("Enter a natural number: "))
print()
n1 = a+1
n2 = a-1
p = None

start_time = time.time()
print("(!) Searching for nearest prime numbers...")
while not p:
    i = 2
    while i <= n1 ** 0.5:
        d = n1 % i
        if d == 0:
            break
        else:
            i += 1
    d = n1 % i
    if d == 0 and n1 != 2:
        p = False
        n1 += 1
    elif d != 0 or n1 <= 3:
        p = True
        break

p = None

while not p:
    i = 2
    while i <= n2 ** 0.5:
        d = n2 % i
        if d == 0:
            break
        else:
            i += 1
    d = n2 % i
    if d == 0 and n2 != 2:
        p = False
        n2 -= 1
    elif d != 0 or n2 <= 3:
        p = True
        break

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
else:
    hrs = int(elapsed_time // 3600000)
    mins = int(elapsed_time // 1) - 3600000 * hrs
    s_mins = mins
    mins = int(mins // 60000)
    secs = s_mins - 60000 * mins
    s_secs = secs
    secs = int(secs // 1000)
    ms = s_secs - 1000 * secs
    elapsed_time = str(hrs) + " h " + str(mins) + " m " + str(secs) + " s " + str(ms) + " ms"

print()
print("[!] The nearest from above:", n1)
print("[!] The nearest from below:", n2)

if int(el_time // 1) != 0:
    print()
    print("(!) Elapsed time:", elapsed_time)
