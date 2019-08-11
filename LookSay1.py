#!/usr/bin/python3
"""Написать последовательность чисел Конвея"""

def LookSay(firstval = 1):
    count = 1
    yield firstval
    currentval = str(firstval) + str(count)
    yield int(currentval)
 
    while True:
        result = ""
        prevval = currentval[0]
        count = 1
        for currentsub in currentval[1:]:
            if prevval != currentsub:
                result += str(count) + str(prevval)
                prevval = currentsub
                count = 1
            else:
                count += 1
        result += str(count) + str(prevval)
        yield int(result)
        currentval = result
         
for i,l in enumerate(LookSay()):
    print(f"{i}: {l}")
    if i>10:
        break
