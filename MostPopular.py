#!/usr/bin/python3
'''
Ввести строку, состоящую из разделённых пробелами последовательностей маленьких и больших латинских букв. 
Вывести, сколько различных слов (без учёта регистра) встречается в этой строке чаще всего.

Input:

dAh Dit dah dIT dAH Dit GIgly diGLy biglY GiGly bOOm quack OH quack
Output:

2



'''
s = str(input())

s1 = s.casefold().split()

s2 = {}.fromkeys(s1,0)

for i in s1:
    s2[i] += 1 

m = max(s2)
count = 0
for i in s2:
    if s2[i] == 3:
        count += 1
print(count)


