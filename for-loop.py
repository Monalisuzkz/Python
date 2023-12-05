import string

#Write a PYTHON Program to produce the following design
"""
A B C D 
A B C D
A B C D 
A B C D 
A B C D
(if user enters n value as 5)
"""

def letters_in_loopinreverse():

    n = int(input("Enter a value:"))

    for i in range(n, 0, -1):
        row  = ' '.join([chr(ord('A') + j) for j in range(i)])
        print(row)
letters_in_loopinreverse()


def letters_in_loopinnotreverse():

    n = int(input("Enter a value:"))

    for i in range(1, n + 1):
        row  = ' '.join([chr(ord('A') + j) for j in range(i)])
        print(row)
letters_in_loopinnotreverse()

def letters_in_samepattern():

    n = int(input("Enter a value:"))

    for i in range(n):
        row  = ' '.join([chr(ord('A') + j) for j in range(0, n + 1)])
        print(row)
letters_in_samepattern()