# -*- coding utf-8 -*-

sal = float(input())

reajuste = {
    2000: 0.04,
    1200: 0.07,
    800: 0.10,
    400: 0.12,
    0: 0.15
}
bonus = 0.0 
porcentagem = 0.0

for i in reajuste.keys():
    if sal > i:
        bonus = sal * reajuste[i]
        porcentagem = reajuste[i] * 100
        break

print(f"Novo salario: {sal + bonus:.2f}\nReajuste ganho: {bonus:.2f}\nEm percentual: {porcentagem:.0f} %")