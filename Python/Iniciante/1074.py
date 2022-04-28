# -*- coding utf-8 -*-

qtd = int(input())

num = []

append = list.append
for i in range(qtd):
    append(num, int(input()))

for i in num:
    if i%2 == 1:
        if i > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
    else:
        if i > 0:
            print("EVEN POSITIVE")
        elif i == 0:
            print("NULL")
        else:
            print("EVEN NEGATIVE")

