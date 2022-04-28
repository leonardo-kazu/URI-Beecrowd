# -*- coding utf-8 -*-

a = int(input())
b = int(input())
soma = aux = 0

if a > b:
    aux = a
    a = b
    b = aux


for i in range((a+1),b):
    if i % 2 != 0:
        soma += i

print(soma)