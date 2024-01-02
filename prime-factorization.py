import time

a = int(input("Enter a natural number: "))
print()

i = 2
factors = []
ofactors = []
start_time = time.time()
while i <= a ** 0.5:
    d = a % i
    if d == 0:
        factors.append(str(i))
        a //= i
    # !! x2 SLOWER !!
    # else:
    #     i += 1
    elif i == 2:
        i += 1
    else:
        i += 2
factors.append(str(a))

for i in range(0, len(factors)):
    if factors[i-1] == factors[i] and len(ofactors) > 0:
        ofactors[-1] = str(ofactors[-1]) + ")"
    else:
        ofactors.append(str(factors[i] + ")"))

for i in range(0, len(ofactors)):
    n = ofactors[i].count(")")
    brackets = n * ")"
    power = "^" + str(n)
    ofactors[i] = ofactors[i].replace(brackets, power)

for i in range(0, len(ofactors)):
    if ofactors[i].find("^1") > 0 and ofactors[i][-2:] == "^1":
        ofactors[i] = ofactors[i].replace("^1", "")

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

result = " · ".join(ofactors)
print(result)

if int(el_time // 1) != 0:
    print()
    print("(!) Elapsed time:", elapsed_time)
