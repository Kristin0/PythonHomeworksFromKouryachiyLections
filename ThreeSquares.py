#!/usr/bin/python3
'''Ввести произвольную последовательность (не обязательно кортеж) натуральных чисел, не превышающих 1000000. Вывести, сколько среди них различных чисел, являющихся суммой трёх квадратов.

Пояснение. Поскольку входная последовательность обрабатывается eval(), она может быть, например, такой: (1+i%10 for i in range(100000)), в этом случае ответ — тоже 3 :)


3, 4, 2, 9, 1, 5, 6, 7, 8, 3, 6

3'''

import math
s = set(eval(input()))

s1 = sorted(s)
m = max(s1)
s2 = set()
for i in s1:
    if i <= math.sqrt(m):
        for j in s1:
            if j <= math.sqrt(m - i**2):
                for k in s1:
                    if k <= math.sqrt(m - i**2 - j**2):
                        s2.add(i*i + j*j + k*k)
                    else: break
            else: break
    else: break   
count = 0
for c in s&s2:
    count+=1
    
print(count)
