# -*- coding utf-8 -*-

contpar = 0
contpos = 0
contneg = 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        contpar += 1
    if num > 0:

        contpos += 1
    elif num < 0:
        contneg += 1
print(f"{contpar} valor(es) par(es)\n{abs(contpar - 5)} valor(es) impar(es)\n{contpos} valor(es) positivo(s)\n{contneg} valor(es) negativo(s)")