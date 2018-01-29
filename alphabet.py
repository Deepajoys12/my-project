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
  ch=input("enter character")
  if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(ch,"is an alphbet")
  else:
    print(ch,"not an alphabet")

if __name__ == '__main__':
    main()
