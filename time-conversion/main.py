#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    times = s.split(":")
    hour_str = times[0]
    minute_str = times[1]
    sec_str = times[2][:2]
    am_pm = times[2][2:]
    
    if am_pm == "AM":
        if hour_str == "12":
            return f"00:{minute_str}:{sec_str}"
        return f"{hour_str}:{minute_str}:{sec_str}"
    else:
        if hour_str == "12":
            return f"12:{minute_str}:{sec_str}"
        new_hour = 12 + int(hour_str)
        return f"{new_hour}:{minute_str}:{sec_str}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
