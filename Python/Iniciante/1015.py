# -*- coding utf-8 -*-

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

print(f"{pow((pow(x1 - x2, 2) + pow(y1 - y2, 2)), 1/2):.4f}")