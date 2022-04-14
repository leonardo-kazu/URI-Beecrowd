# -*-coding utf-8 -*-

a, b, c = map(float, input().split())

triangulo = lambda base, altura: base * altura / 2
circulo = lambda raio: 3.14159 * raio.__pow__(2)
trapezio = lambda base_m, base_p, altura: (base_m + base_p) * altura / 2
quadrado = lambda lado: lado.__pow__(2)
retangulo = lambda base, altura: base * altura

print(f"TRIANGULO: {triangulo(a, c):.3f}\nCIRCULO: {circulo(c):.3f}\nTRAPEZIO: {trapezio(a, b, c):.3f}\nQUADRADO: {quadrado(b):.3f}\nRETANGULO: {retangulo(a, b):.3f}")