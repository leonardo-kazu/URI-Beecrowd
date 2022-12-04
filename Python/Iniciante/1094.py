# -*- coding utf-8 -*-


def main():
    subjects = {
        'C': 0,
        'R': 0,
        'S': 0
    }

    runs = int(input())
    num = ''
    subject = ''
    for i in range(runs):
        num, subject = input().split()
        subjects[subject] += int(num)

    total = subjects['C'] + subjects['R'] + subjects['S']
    print(f"Total: {total} cobaias\nTotal de coelhos: {subjects['C']}\nTotal de ratos: {subjects['R']}\nTotal de sapos: {subjects['S']}\nPercentual de coelhos: {subjects['C']*100/total:.2f} %\nPercentual de ratos: {subjects['R']*100/total:.2f} %\nPercentual de sapos: {subjects['S']*100/total:.2f} %")


if __name__ == "__main__":
    main()
