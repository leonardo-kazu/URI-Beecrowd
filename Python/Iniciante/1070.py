# -*- coding utf-8 -*-

num = int(input())

if num % 2 == 1:
    for i in range(6):
        print(num)
        num += 2
else:
    num += 1
    for i in range(6):
        print(num)
        num += 2