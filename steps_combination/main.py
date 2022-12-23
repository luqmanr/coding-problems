""" 5
1,1,1,1,1
1,1,1,2
1,1,3
1,3,1
3,1,1
1,1,2,1
1,2,1,1
1,2,2
2,1,1,1
2,1,2
2,2,1
2,3
3,2
"""

def soul(steps_limit, steps_num=[1,2,3]):
    num = 0
    for step_num in steps_num:
        mod = steps_limit // step_num
        num += step_num**mod

    return num

print(soul(5, [1,2,3]))