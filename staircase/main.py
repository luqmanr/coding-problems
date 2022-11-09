#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1, n+1):
        first_half = n - i
        last_half = i
        new_str = ""
        for k in range(first_half):
            new_str += " "
        for k in range(last_half):
            new_str += "#"
        print(new_str)
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
