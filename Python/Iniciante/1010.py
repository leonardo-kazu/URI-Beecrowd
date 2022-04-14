# -*- coding utf-8 -*-

cod_um, num_um, valor_um = map(float, input().split()) #Usando o método split()

cod_dois, num_dois, valor_dois = [float(x) for x in input().split()] #Usando list comprehension

print(f"VALOR A PAGAR: R$ {((num_um * valor_um) + (num_dois * valor_dois)):.2f}")