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
  yr=int(input("enter the year"))
  if(yr%4==0):
    print(yr,"this is leap year")
  else:
    print(yr,"not leap year")


if __name__ == '__main__':
    main()
