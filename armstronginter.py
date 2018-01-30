#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Deepa
#
# Created:     30/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 lower = int(input("Enter lower range: "))
 upper = int(input("Enter upper range: "))

 for num in range(lower,upper + 1):
  sum = 0
  temp = num
  while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

  if num == sum:
       print(num)

if __name__ == '__main__':
    main()
