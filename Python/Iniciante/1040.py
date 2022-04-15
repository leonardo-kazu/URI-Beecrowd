# -*- coding utf-8 -*-

n1, n2, n3, n4 = map(float, input().split())
media = (n1*2 + n2*3 + n3*4 + n4*1)/10

if media > 6.9:
    print(f"Media: {media:.1f}\nAluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}\nAluno reprovado.")
else:
    exame = float(input())
    print(f"Media: {media:.1f}\nAluno em exame.")
    print(f"Nota do exame: {exame:.1f}")
    final = (exame + media)/2
    if final >= 5:
        print(f"Aluno aprovado.\nMedia final: {final:.1f}")
    else:
        print(f"Aluno reprovado.\nMedia final: {final:.1f}")

