# -*- coding utf-8 -*-

def time(entry):
    i = 0
    while (i in range(len(entry))):
        try:
            entry[i] = int(entry[i])
        except:
            entry.pop(i)
            i -= 1
        i += 1
    return entry


first_day = time([x for x in input().split()])
time_first = time([x for x in input().split()])

second_day = time([x for x in input().split()])
time_second = time([x for x in input().split()])

passed_time = [0, 0, 0, 0]

if time_first[2] <= time_second[2]:
    passed_time[3] = time_second[2] - time_first[2]
else:
    passed_time[3] = time_second[2] - time_first[2] + 60
    time_first[1] += 1

if time_first[1] <= time_second[1]:
    passed_time[2] = time_second[1] - time_first[1]
else:
    passed_time[2] = time_second[1] - time_first[1] + 60
    time_first[0] += 1

if time_first[0] <= time_second[0]:
    passed_time[1] = time_second[0] - time_first[0]
    
else:
    passed_time[1] = time_second[0] - time_first[0] + 24
    first_day[0] += 1

passed_time[0] = second_day[0] - first_day[0]

print(f"{passed_time[0]} dia(s)")
print(f"{passed_time[1]} hora(s)")
print(f"{passed_time[2]} minuto(s)")
print(f"{passed_time[3]} segundo(s)")