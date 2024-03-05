#!/usr/bin/python3

l  = open(0)
result = []
for i in l:
    string = "&emsp;"
    change = True
    for j in i:
        if j != ' ':
            change = False
        if not change:
            string += j
        elif j == " ":
            string += "&;"
    result += [string]

for i in result:
    print(i.strip())


