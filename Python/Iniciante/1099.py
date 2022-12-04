# -*- coding: utf-8 -*-

def main():
    case = int(input())
    for i in range(case):
        low, high = map(int, input().split())

        if low > high:
            low, high = high, low

        sum = 0
        for num in range(low+1, high):
            if num % 2 != 0:
                sum += num

        print(sum)


if __name__ == '__main__':
    main()
