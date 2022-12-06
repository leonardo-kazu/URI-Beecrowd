# -*- coding: utf-8 -*-

def main():
    # Variavies
    low = int(input())
    high = int(input())
    if low > high:
        low, high = high, low

    soma = 0

    # Loop principal
    for i in range(low, high+1):
        soma += i if i % 13 != 0 else 0
    print(soma)


if __name__ == '__main__':
    main()
