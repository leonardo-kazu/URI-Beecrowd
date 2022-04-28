# -*- coding utf-8 -*-

qtd = int(input())
num_in = num = 0
for i in range(qtd):
    num = int(input())
    num_in += 1 if num >= 10 and num <= 20 else 0

print(f"{num_in} in\n{abs(num_in - qtd)} out")