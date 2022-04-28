# -*- coding utf-8 -*-

num = int(input())
quad = pow
for i in range(2, num + 1, 2):
    print(f"{i}^2 = {quad(i,2)}")

