# -*- coding utf-8 -*-
num = 0
for i in range(5):
    num += 1 if int(input()) % 2 == 0 else 0
print(f"{num} valores pares")