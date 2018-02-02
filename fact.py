#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Deepa
#
# Created:     02/02/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

if __name__ == '__main__':

    factorial(n)
