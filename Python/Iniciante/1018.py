# -*- coding utf-8 -*-

def calc(valor, total):
    aux = total // valor
    print(f"{aux} nota(s) de R$ {valor:.2f}")
    return valor * aux

x = int((input()))

valores = [100, 50, 20, 10, 5, 2, 1]

for i in valores:
    x -= calc(i, x) 

