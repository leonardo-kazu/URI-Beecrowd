# -*- coding: utf-8 -*-

def main():
    cont = 0
    media = 0
    while True:
        nota = float(input())

        if nota > 10 or nota < 0:
            continue
        media += nota
        cont += 1
        if cont == 2:
            print(f'media = {media/2:.2f}')
            break


if __name__ == '__main__':
    main()
