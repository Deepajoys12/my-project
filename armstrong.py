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
 n=int(input("Enter any number: "))
 a=list(map(int,str(n)))
 b=list(map(lambda x:x**3,a))
 if(sum(b)==n):
    print(n," is an armstrong number. ")
 else:
    print(n," isn't an arsmtrong number. ")

if __name__ == '__main__':
    main()
