#!/usr/bin/python3
import hidden_4

def discovr():
    mylist = dir(hidden_4)
    for i in mylist:
        if i[:2] != '__':
            print("{:s}".format(i))

if __mylist__ == "__main__":
    discovr()
