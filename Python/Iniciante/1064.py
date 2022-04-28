# -*- coding utf-8 -*-
total = list()

for i in range(6):
    num = float(input()) 
    if num > 0:
        total.append(num)
    
print(f"{len(total)} valores positivos\n{sum(total)/len(total):.1f}")
    