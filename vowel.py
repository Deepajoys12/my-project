#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Deepa
#
# Created:     23/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
     l = input("enter a letter of the alphabet: ")

     if l in ('a', 'e', 'i', 'o', 'u'):
     	print("%s is a vowel." % l)
     elif l == 'y':
     	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
     else:
	     print("%s is a consonant." % l)

if __name__ == '__main__':
    main()
