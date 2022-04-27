# -*- coding utf-8 -*-

sal = float(input()) - 2000

taxas = {
    8: 0.08,
    18: 0.18,
    28: 0.28
}

if(sal <= 0):
    print("Isento")
else:
    if(sal > 2500):
        sal -= 2500
        print(f"R$ {sal*taxas[28] + 1500*taxas[18] + 1000*taxas[8] :.2f}")
    elif(sal > 1000):
        sal -= 1000
        print(f"R$ {sal*taxas[18] + 1000*taxas[8] :.2f}")
    else:
        print(f"R$ {sal*taxas[8]:.2f}")