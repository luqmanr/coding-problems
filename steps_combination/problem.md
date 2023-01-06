# Question
Given a number of steps (eg. 10, or 6, or 255 -> basically real numbers)
Return how many number of combinations a person can take, if a person
can take 1, 2, or 3 steps at a time to reach the last step

# Note
The person must reach the last step

# Example
Number of steps: 5
Combinations: [
    [1,2,2],
    [2,1,2],
    [2,2,1],
    [2,3],
    [3,2],
    [3,1,1],
    [1,1,3],
    [1,3,1],
    [1,1,1,1,1],
    [1,1,1,2],
    [1,1,2,1],
    [1,2,1,1],
    [2,1,1,1]
]
Return = 13

# Solution Cheat:
https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/