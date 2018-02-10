#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     10/02/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

   def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)

    if m != n:
        return False


   marked = [False] * MAX_CHARS


   map = [-1] * MAX_CHARS

   for i in xrange(n):


        if map[ord(string1[i])] == -1:


            if marked[ord(string2[i])] == True:
                return False


            marked[ord(string2[i])] = True


            map[ord(string1[i])] = string2[i]


        elif map[ord(string1[i])] != string2[i]:
            return False

   return True
   print (areIsomorphic("aab","xxy"))
   print (areIsomorphic("aab","xyz"))


if __name__ == '__main__':
    main()
