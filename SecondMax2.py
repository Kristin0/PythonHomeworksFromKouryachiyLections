#!/usr/bin/python3.7
S=eval(input())

max1=max2=0

for i in S:
    a = False
    if i > max1:
        max2 = max1
        max1 = i
    elif i >= max2 and i < max1:
        max2 = i
        a = True

if max2==0 and a== False:
    print("no max")
else:
    print(max2)
