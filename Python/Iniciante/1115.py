# -*- coding: utf-8 -*-

def main():
    x, y = map(int, input().split())
    if x > 0:
        if y > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if y > 0:
            print('segundo')
        else:
            print('terceiro')


if __name__ == '__main__':
    main()
