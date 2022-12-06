# -*- coding: utf-8 -*-

def main():
    run = True
    while run:
        cont = 0
        media = 0
        while True:
            nota = float(input())

            if nota > 10 or nota < 0:
                print(f'nota invalida')
                continue

            media += nota
            cont += 1

            if cont == 2:
                print(f'media = {media/2:.2f}')
                break

        while True:
            print('novo calculo (1-sim 2-nao)')
            escolha = int(input())
            if escolha == 1:
                break
            elif escolha == 2:
                run = False
                break


if __name__ == '__main__':
    main()
