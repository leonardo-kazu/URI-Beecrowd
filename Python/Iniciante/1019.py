# -*- coding utd-8 -*-

def main():
    time = int(input())
    calc = lambda total, valor: total // valor
    hours = calc(time, 3600)
    time -= hours * 3600
    minutes = calc(time, 60)
    time -= minutes * 60
    print(f"{hours}:{minutes}:{time}")

if __name__ == "__main__":
    main()
