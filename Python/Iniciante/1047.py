# -*- coding utf-8 -*-

h1, m1, h2, m2 = map(int, input().split())

if h1 == h2 and m1 == m2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if m1 <= m2:
        print(f"O JOGO DUROU {(24-h1+h2)%24} HORA(S) E {(60-m1+m2)%60} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {(23-h1+h2)%24} HORA(S) E {(60-m1+m2)%60} MINUTO(S)")