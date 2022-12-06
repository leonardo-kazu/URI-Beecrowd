# -*- coding: utf-8 -*-

def main():
    # Variaveis
    low = int(input())
    high = int(input())
    if low > high:
        low, high = high, low

    for i in range(low + 1, high):
        if i % 5 == 2 or i % 5 == 3:
            print(i)


if __name__ == '__main__':
    main()
