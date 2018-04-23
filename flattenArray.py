#!/usr/bin/env python

import sys
from testList import *

def flatten(input, result):
        for i in input:
                print(i)
                if type(i) == type([]):
                        flatten(i, result)
                else:
                        result+=i
                        print(result)
        return result

print(flatten(input, store))

#print("First parameter: ", sys.argv[1])
#print("Second parameter: ", sys.argv[2])
#print flatten(sys.argv[1], sys.argv[2])
