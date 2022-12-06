# -*- coding: utf-8 -*-

def main():
    # Variaveis
    alcool = 0
    gasolina = 0
    diesel = 0

    # Loop principal
    while True:
        escolha = int(input())
        if escolha == 1:
            alcool += 1
        elif escolha == 2:
            gasolina += 1
        elif escolha == 3:
            diesel += 1
        elif escolha == 4:
            break

    # Apresentação
    print('MUITO OBRIGADO')
    print(f'Alcool: {alcool}')
    print(f'Gasolina: {gasolina}')
    print(f'Diesel: {diesel}')


if __name__ == '__main__':
    main()
