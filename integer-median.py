# This program finds triangles with natural sides and almost natural medians

import time

a = 1
b = 1
c = 1
counter = 0
show = None
range = int(input("Введите диапазон (натуральное число): "))
print()
start_time = time.time()
while c <= range:
    while b <= range:
        while a <= range:
            if a<b+c and b<a+c and c<a+b:
                m1 = 0.5 * (2 * a ** 2 + 2 * b ** 2 - c ** 2) ** 0.5
                m2 = 0.5 * (2 * a ** 2 + 2 * c ** 2 - b ** 2) ** 0.5
                m3 = 0.5 * (2 * c ** 2 + 2 * b ** 2 - a ** 2) ** 0.5
                if (100*m1 // 1) == 100*m1 and (100*m2 // 1) == 100*m2 and (100*m3 // 1) == 100*m3:
                    show = True
                else:
                    show = False
                if show == True:
                    print("[!] Треугольник (", a, ", ", b, ", ", c, ") имеет медианы: ", m1, ", ", m2, ", ", m3, sep="")
                    counter += 1
                a += 1
            else:
                break
        b += 1
        a = b
    c += 1
    b = c
    a = b

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
print("(!) Всего треугольников:", counter)
if int(el_time // 1) != 0:
    print()
    print("(!) Elapsed time:", elapsed_time)