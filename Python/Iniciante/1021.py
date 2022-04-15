# -*- coding utf-8 -*-

def calc(total, valor, tipo):
    aux = total // valor
    print(f"{aux:.0f} {tipo} de R$ {valor:.2f}")
    return valor * aux

valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
tipo = ["nota(s)", "moeda(s)"]
total = float(input())
print("NOTAS:")

for i in valores:
    if i == 1:
        print("MOEDAS:")
    total -= calc(total, i, tipo[0] if i > 1 else tipo[1])