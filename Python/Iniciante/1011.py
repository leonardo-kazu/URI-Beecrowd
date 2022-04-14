# -*- coding utf-8 -*-

raio = int(input())
pi = 3.14159

volume = lambda pi, r: (4.0/3) * pi * r.__pow__(3)

print(f"VOLUME = {volume(pi, raio):.3f}")