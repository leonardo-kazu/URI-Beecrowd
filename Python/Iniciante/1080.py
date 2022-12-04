# -*- coding utf-8 -*-

maior = aux = pos = 0

for i in range(100):
    aux = int(input())
    if aux > maior:
        pos = i + 1
        maior = aux

print(maior)
print(pos)
