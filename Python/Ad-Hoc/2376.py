# BeeCrowd 2376

# Entradas de todas as partidas(esquerda e direita pensando de acordo com 
# imagem)
jogo_1_A, jogo_1_B = map(int, input().split())
jogo_2_C, jogo_2_D = map(int, input().split())
jogo_3_E, jogo_3_F = map(int, input().split())
jogo_4_G, jogo_4_H = map(int, input().split())
jogo_5_I, jogo_5_J = map(int, input().split())
jogo_6_K, jogo_6_L = map(int, input().split())
jogo_7_M, jogo_7_N = map(int, input().split())
jogo_8_O, jogo_8_P = map(int, input().split())

jogo_9_esq, jogo_9_dir = map(int, input().split())
jogo_10_esq, jogo_10_dir = map(int, input().split())
jogo_11_esq, jogo_11_dir = map(int, input().split())
jogo_12_esq, jogo_12_dir = map(int, input().split())

jogo_13_esq, jogo_13_dir = map(int, input().split())
jogo_14_esq, jogo_14_dir = map(int, input().split())

jogo_15_esq, jogo_15_dir = map(int, input().split())


# Começando as verificações do último jogo descendo até o primeiro
# checa qual lado ganhou o jogo de numero X e partir dele escolhe qual lado
# das opções de jogos descer até chegar no time vitorioso
if(jogo_15_dir > jogo_15_esq):
    if(jogo_14_dir > jogo_14_esq):
        if(jogo_12_dir > jogo_12_esq):
            if(jogo_8_P > jogo_8_O):
                print("P")
            else:
                print("O")

        else:
            if(jogo_7_N > jogo_7_M):
                print("N")
            else:
                print("M")

    else:
        if(jogo_11_dir > jogo_11_esq):
            if(jogo_6_L > jogo_6_K):
                print("L")
            else:
                print("K")

        else:
            if(jogo_5_J > jogo_5_I):
                print("J")
            else:
                print("I")
else:
    if(jogo_13_dir > jogo_13_esq):
        if(jogo_10_dir > jogo_10_esq):
            if(jogo_4_H > jogo_4_G):
                print("H")
            else:
                print("G")

        else:
            if(jogo_3_F > jogo_3_E):
                print("F")
            else:
                print("E")

    else:
        if(jogo_9_dir > jogo_9_esq):
            if(jogo_2_D > jogo_2_C):
                print("D")
            else:
                print("C")

        else:
            if(jogo_1_B > jogo_1_A):
                print("B")
            else:
                print("A")