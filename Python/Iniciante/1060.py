# -*- coding utf-8 -*-
control = 0
for i in range(6):
    num = float(input())
    control += 1 if num > 0 else 0
print(f"{control} valores positivos")
        