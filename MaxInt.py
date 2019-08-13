#!/usr/bin/python3
"""

Ввести текст, состоящий из нескольких строк (заканчивается пустой строкой). Каждая строка состоит из «слов» (последовательностей непробельных символов), разделённых пробелами или табуляциями. Некоторые слова — целые числа (возможно, отрицательные), другие числами не являются (хотя могут содержать цифры). Найти и вывести наибольшее из этих чисел.

Input:

enemies -565 glanduliform h252Tbeaic -tv5naa2re4 55 silicamortar eared
ra50ertc-8 -4 94 ohgutyd38 163 -562 u8e8qisn handout crossword 22s4cico
-v80s6eessl beaning en1A1i-2l 545 december flo ch00a0-h1t vignettist
­­
Output:

545
"""

l = ""
l2 = []
while(True):
    S = str(input())
    l += S
    if not S:
        break
l1 = l.split()
for i in l1:
    if (i[0] == '-' and i[1:].isdecimal() or i.isdecimal()):
        l2 += [int(i)]

print(max(l2))

