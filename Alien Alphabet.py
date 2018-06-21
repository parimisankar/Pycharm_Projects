'''Alien Alphabet
Aliens visited earth and their alphabets are very weird.
Its the same 26 letters (A to Z) but in a different order.
They want your help to sort a string in the order of their alphabet.

Aliens might use the reversed alphabet of "zyxwvutsrqponmlkjihgfedcba"
so when they sort "abc", it becomes "cba" and when they sort "apple" it becomes "pplea".

When sorted capital/lowercase letters, the capital letters always comes first (e.g. "camelCasE" -> "smlEeCcaa").

You will write a program that reads 2 lines from standard input
- the first line is the alien's alphabet (letters a-z, all lowercase)
- the second line is the string the aliens want you to sort.
- Your program will output the sorted string.

Examples are provided below.
Example 1
input
abcdefghijklmnopqrstuvwxyz
cyxbza

output
abcxyz

Example 2
input
zyxwvutsrqponmlkjihgfedcba
cyxbza

output
zyxcba

Example 3
input
wvutsrqponmlkjihgfedcbaxyz
camelCasE

output
smlEeCcaa
'''

from sys import stdin
s1 = stdin.readline()
s2 = stdin.readline()

indexs = []
flag = []
for a in s2:
    if a in s1:
        i = s1.index(a.lower())
        indexs.append(i)
    elif a.lower() in s1:
        i = s1.index(a.lower())
        indexs.append(i)
        flag.append(i)
    else:
        exit("Input Error")
indexs.sort()

answerList = []
for i in indexs:
    if i in flag:
        answerList.append(s1[i].upper())
        flag.pop(flag.index(i))
    else:
        answerList.append(s1[i])
answer = ''.join(answerList)
print(answer)