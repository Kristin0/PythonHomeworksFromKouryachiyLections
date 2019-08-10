"""Ввести небольшое натуральное число 2⩽N⩽1000000 и проверить, является ли оно степенью натурального числа (>1). Вывести YES или NO соответственно.

Input:

1024
Output:

YES"""

#!/usr/bin/python3.7
num=eval(input())

def func(num):
    for i in range(2,1000):
        for j in range(2,10):
            if(i**j == num):
              return "YES"
    return "NO"     
   
print(func(num))    
