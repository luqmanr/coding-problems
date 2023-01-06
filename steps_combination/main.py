def soul(steps_limit, steps_num=[1,2,3]):
    steps_taken = []
    remaining_steps = steps_limit
    index_step = 0
    while remaining_steps > 0:
        remaining_steps = remaining_steps - steps_num[::-1][index_step]
        if remaining_steps < 0:
            remaining_steps += steps_num[::-1][index_step]
            index_step -= 1
        else:
            steps_taken.append(steps_num[::-1][index_step])
            index_step += 1
            print("remaining steps:", remaining_steps)
    
    print("steps taken:", steps_taken)

# soul(5)

def countWays(n):
    res = [0] * (n + 2)
    print("res:", res)
    res[0] = 1
    res[1] = 1
    res[2] = 2
    print("res:", res)
 
    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
 
    return res[n]
 
 
# Driver code
n = 5
print(countWays(n))