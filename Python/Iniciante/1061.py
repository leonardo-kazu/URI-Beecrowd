# -*- coding utf-8 -*-

# first_day = int(input().strip("Dia"))
time_first = [x for x in input().split()]
for char in time_first:
    if char == ":":
        time_first.remove(char)
        
print(time_first)