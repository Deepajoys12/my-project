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
 num =int(input("enter a number"))
 if num > 1:

     for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")

           break
     else:
       print(num,"is a prime number")


 else:
   print(num,"is not a prime number")

if __name__ == '__main__':
    main()
