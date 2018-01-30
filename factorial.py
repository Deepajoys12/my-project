#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     31/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 num = int(input("enter a number"))
 factorial = 1
 if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
 elif num == 0:
   print("The factorial of 0 is 1")
 else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

if __name__ == '__main__':
    main()
