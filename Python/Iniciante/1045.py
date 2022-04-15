# -*- coding utf-8 -*-

num = sorted([float(x) for x in input().split()], reverse=True)


if not(num[0] < num[1] + num[2]):
    print("NAO FORMA TRIANGULO")
else:
    if num[0].__pow__(2) == num[1].__pow__(2) + num[2].__pow__(2):
        print("TRIANGULO RETANGULO") 
    if num[0].__pow__(2) > num[1].__pow__(2) + num[2].__pow__(2):
        print("TRIANGULO OBTUSANGULO") 
    if num[0].__pow__(2) < num[1].__pow__(2) + num[2].__pow__(2):
        print("TRIANGULO ACUTANGULO") 
    if num[0] == num[1] and num[2] == num[1]:
        print("TRIANGULO EQUILATERO")  
    if (num[0] != num[1] and num[1] == num[2]) or (num[1] != num[2] and num[2] == num[0]) or (num[2] != num[1] and num[1] == num[0]):
        print("TRIANGULO ISOSCELES") 