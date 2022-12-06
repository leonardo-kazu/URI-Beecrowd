# -*- coding: utf-8 -*-

def main():
    # Declarando variaveis para apresentação de dados finais
    win_inter = 0
    win_gremio = 0
    empate = 0

    # Loop principal
    while True:
        inter, gremio = map(int, input().split())

        # Contabilização de estatisticas
        if inter > gremio:
            win_inter += 1
        elif gremio > inter:
            win_gremio += 1
        else:
            empate += 0

        # Verificação de continuação do loop
        print('Novo grenal (1-sim 2-nao)')
        escolha = int(input())
        if escolha == 1:
            continue
        else:
            break

    # Lógica de apresentação dos dados
    print(f'{win_inter + win_gremio + empate} grenais')
    print(f'Inter:{win_inter}')
    print(f'Gremio:{win_gremio}')
    print(f'Empates:{empate}')
    if win_inter > win_gremio:
        print('Inter venceu mais')
    elif win_gremio > win_inter:
        print('Gremio venceu mais')
    else:
        print('Não houve vencedores')


if __name__ == '__main__':
    main()
