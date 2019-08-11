#!/usr/bin/python3.7
"""
Написать генератор LookSay() цифр последовательности Конвея «Look and Say». (Сама последовательность Конвея). Описание в Википедии

for i,l in enumerate(LookSay()):
    print(f"{i}: {l}")
    if i>10:
        break

0: 1
1: 1
2: 1
3: 2
4: 1
5: 1
6: 2
7: 1
8: 1
9: 1
10: 1
11: 1 """
def LookSay(firstval = 1):
    yield 1
    count = 1
    yield count
    currentval = str(firstval) + str(count)
    yield int(firstval)
    while True:
        result = ""
        prevval = currentval[0]
        count = 1
        for currentsub in currentval[1:]:
            if prevval != currentsub:
                yield count
                yield int(prevval)
                result += str(count) + str(prevval) 
                prevval = currentsub
                count = 1             
                
            else: 
                count += 1 
               
                
        yield count
        yield int(prevval) 
        result += str(count) + str(prevval)
        
        currentval = result    
         
for i,l in enumerate(LookSay()):
    print(f"{i}: {l}")
    if i>28:
        break

