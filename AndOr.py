#!/usr/bin/python3.7
"""Ввести два объекта Python и вывести первый непустой из них. 
Если оба пустые, вывести NO.
Input:
[]
123
Output:
123"""
a,b=eval(input())
if(not a and not b):
   print("no")
else:
   print(a or b)
