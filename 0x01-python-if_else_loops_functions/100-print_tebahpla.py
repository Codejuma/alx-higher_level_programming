#!/usr/bin/python3
a = 122
while a >= 97:
    flag = 0
    if a % 2 != 0:
        a = a - 32
        flag = 1
    print("{:s}".format(chr(a)), end="")
    if flag == 1:
        a = a + 32
    a = a - 1
