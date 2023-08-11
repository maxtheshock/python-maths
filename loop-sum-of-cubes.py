import math
import time

a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))

print()
s = a
n1 = 1
counter = 0
isRepresentable = None

start_time = time.time()
cyc1_time = start_time
while a <= b:
    while n1 <= round(((4 * a) ** (1/3)) * 0.5) and a - (n1 ** 3) > 0:
        n2 = (a - (n1 ** 3)) ** (1/3)
        n3 = round(n2)
        if n1 ** 3 + n3 ** 3 == a and n3 >= n1:
            isRepresentable = True
            break
        else:
            n1 += 1
    cyc2_time = time.time()
    n1 = 1
    if isRepresentable == True:
        # print("[!] Number", a, "can be represented")
        counter += 1
    isRepresentable = False
    if cyc2_time - cyc1_time > 1:
        print("(!) Progress: ", 100 * (a - s + 1) / (b - s + 1), "%", sep="")
        cyc1_time = cyc2_time
    a += 1

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

if int(el_time // 1) != 0:
    print()
    print("(!) Elapsed time:", elapsed_time)
print()
print("[!] General amount:", counter)
