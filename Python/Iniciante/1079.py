# -*- coding utf-8 -*-

qtd = int(input())
nums = []
append = list.append
for i in range(qtd):
        append(nums, [float(x) for x in input().split()])
        
soma = sum
for i in range(qtd):
        nums[i][0] *= 0.2
        nums[i][1] *= 0.3
        nums[i][2] *= 0.5
        print(f"{soma(nums[i]):.1f}")