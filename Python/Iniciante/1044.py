# -*- coding utf-8 -*-

num = sorted([int(x) for x in input().split()])
print("Sao Multiplos") if num[1] % num[0] == 0 else print("Nao sao Multiplos")