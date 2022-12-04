# -*- coding: utf-8 -*-

def main():
    qtd = int(input())

    for i in range(qtd):
        num1, num2 = map(int, input().split())
        if num2 == 0:
            print('divisao impossivel')
        elif num1 == 0:
            print('0.0')
        else:
            print(num1/num2)


if __name__ == '__main__':
    main()
