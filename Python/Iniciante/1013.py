# -*- coding utf-8 -*-

a, b, c = map(int, input().split())

maior = lambda a, b : (a + b + abs(a - b)) / 2

print(f"{int(maior(c, maior(a, b)))} eh o maior")