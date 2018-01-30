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
 lower=int(input("enter a lower number"))
 upper=int(input("enter a upper number"))
 for num in range(lower,upper + 1):
  if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

 if num == sum:
       print(num)

if __name__ == '__main__':
    main()
