# -*- coding: utf-8 -*-

def main():
    for i in range(0, 21, 2):
        for j in range(1, 4):
            x = j+i/10
            if i % 10 == 0:
                print(f'I={int(i/10)} J={int(x)}')
            else:
                print(f'I={i/10} J={x:.2}')


if __name__ == '__main__':
    main()
