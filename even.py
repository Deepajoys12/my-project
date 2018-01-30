#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     30/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 lower=int(input("Enter the starting number:"))
 upper=int(input("Enter the ending number:"))
 for i in range(lower,upper):
    if(i%2!=0):
        print(i)

if __name__ == '__main__':
    main()
