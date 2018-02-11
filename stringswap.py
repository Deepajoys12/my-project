#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     11/02/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def separate_string(sentence):
     l = list(sentence)
     l2 = list()
     for letter in range(l):
        index = l.index(letter)
        if index % 2 != 0:
            l2.append(l[letter])
            l.remove(letter)
if __name__ == '__main__':
    separate_string('abcedfg')
