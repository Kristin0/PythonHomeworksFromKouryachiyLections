#!/usr/bin/python3.7
number=eval(input())
t=tuple(number)
for i in t:
    if i%2==0:
        t+=t[i]
    else:
        t.
print(t)

