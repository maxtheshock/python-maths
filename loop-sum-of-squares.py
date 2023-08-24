import math
import time

show = None
fails = 0
deny = None

a = input("Enter the lower bound: ")
for i in a:
    if i == "." or i == "-":
        deny = True
        break
    else:
        deny = False

while deny:
    fails += 1
    a = input("Enter a NATURAL number: ")
    for i in a:
        if i == "." or i == "-":
            deny = True
            break
        else:
            deny = False

if fails > 0:
    print()
    fails = 0

a = int(a)
deny = None
deny1 = True

b = input("Enter the upper bound: ")

for i in b:
    if i == "." or i == "-":
        deny = True
        break
    else:
        deny = False
if eval(b) < a:
    deny1 = True
else:
    deny1 = False

while deny or deny1:
    fails += 1
    while deny:
        b = input("Enter a NATURAL number: ")
        for i in b:
            if i == "." or i == "-":
                deny = True
                break
            else:
                deny = False

    if eval(b) < a:
        deny1 = True
    else:
        deny1 = False

    while deny1:
        b = input("Upper bound must be GREATER than the lower one: ")
        if eval(b) < a:
            deny1 = True
            break
        else:
            deny1 = False

    for i in b:
        if i == "." or i == "-":
            deny = True
            break
        else:
            deny = False

if fails > 0:
    print()
    fails = 0

b = int(b)
del deny, deny1
if show:
    print()
    del show

numsDisplayed = input("Do we need to display numbers? (Y/N)\n")
while numsDisplayed != "Y" and numsDisplayed != "y" and numsDisplayed != "N" and numsDisplayed != "n":
    numsDisplayed = input("Do we need to display numbers? (Y/N)\n")
if numsDisplayed == "Y" or numsDisplayed == "y":
    print()

x = a
n1 = 1
counter = 0
isRepresentable = None
timeDisplayed = None

start_time = time.time()
cyc1_time = start_time
while a <= b:
    while n1 <= ((2 * a) ** 0.5) * 0.5:
        n2 = (a - n1 ** 2) ** 0.5
        n3 = math.floor(n2)
        if n2 == n3 and n1 ** 2 + n3 ** 2 == a:
            isRepresentable = True
            break
        else:
            n1 += 1
    cyc2_time = time.time()
    n1 = 1
    if isRepresentable == True:
        if numsDisplayed == "Y" or numsDisplayed == "y":
            print("[!] Number", a, "can be represented")
        counter += 1
    isRepresentable = False
    if cyc2_time - cyc1_time > 1 and timeDisplayed != True:
        print()
        print("(!) Progress: ", 100 * (a - x + 1)/(b - x + 1), "%", sep="")
        timeDisplayed = True
        cyc1_time = cyc2_time
    elif cyc2_time - cyc1_time > 1 and timeDisplayed == True:
        print("(!) Progress: ", 100 * (a - x + 1)/(b - x + 1), "%", sep="")
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
