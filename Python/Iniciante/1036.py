# -*- coding utf-8 -*-

a, b, c = map(float, input().split())

delta = b.__pow__(2) - 4*a*c

if delta < 0 or delta.__pow__(0.5) == b:
    print("Impossivel calcular")
else:
    print(f"R1 = {(-b + delta.__pow__(0.5)) / (2 * a):.5f}")
    print(f"R2 = {(-b - delta.__pow__(0.5)) / (2 * a):.5f}")