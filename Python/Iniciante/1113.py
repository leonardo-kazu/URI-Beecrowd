# -*- coding: utf-8 -*-

def main():
    while True:
        low, high = map(int, input().split())
        if low == high:
            break

        if low > high:
            print('Decrescente')
        else:
            print('Crescente')


if __name__ == "__main__":
    main()
