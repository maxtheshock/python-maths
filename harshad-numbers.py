import time

a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))
timeDisplayed = None
s = a
amount = 0
s = 0

start_time = time.time()
cyc1_time = start_time
while a <= b:
    string = str(a)
    digits = []
    for n in string:
        n = int(n)
        digits.append(n)
    for n in digits:
        s += n
    cyc2_time = time.time()
    d = a % s
    if d == 0:
        print("[!] Number", a, "is harshad")
        amount += 1
    if cyc2_time - cyc1_time > 1 and timeDisplayed != True:
        print()
        print("(!) Progress: ", 100 * (a - s + 1) / (b - s + 1), "%", sep="")
        timeDisplayed = True
        cyc1_time = cyc2_time
    elif cyc2_time - cyc1_time > 1 and timeDisplayed == True:
        print("(!) Progress: ", 100 * (a - s + 1) / (b - s + 1), "%", sep="")
        cyc1_time = cyc2_time
    s = 0
    digits.clear()
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
print("General amount:", amount)