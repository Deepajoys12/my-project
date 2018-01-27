#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     27/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])

if __name__ == '__main__':
    main()
