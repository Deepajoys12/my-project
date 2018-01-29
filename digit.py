#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     29/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 n=int(input("Enter number:"))
 count=0
 while(n>0):
    count=count+1
    n=n//10
 print("The number of digits in the number are:",count)

if __name__ == '__main__':
    main()
