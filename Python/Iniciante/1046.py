# -*- coding utf-8 -*-

a, b = map(int, input().split())
if a == b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print(f"O JOGO DUROU {(24-a+b)%24} HORA(S)")