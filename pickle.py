#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Deepa
#
# Created:     19/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 try:
    import cPickle as pickle
 except:
    import pickle
 import pprint

 data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
 print ('DATA:',)
 pprint.pprint(data)

 data_string = pickle.dumps(data)
 print ('PICKLE:', data_string)
if __name__ == '__main__':
    main()
