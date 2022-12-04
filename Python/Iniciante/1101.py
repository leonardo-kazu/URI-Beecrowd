# -*- coding: utf-8 -*-

def main():
    while True:
        low, high = map(int, input().split())

        if low > high:
            low, high = high, low

        if low <= 0:
            break

        nums = [int(x) for x in range(low, high+1)]

        for i in nums:
            print(f'{i}', end=' ')
        print(f'Sum={sum(nums)}')


if __name__ == '__main__':
    main()
