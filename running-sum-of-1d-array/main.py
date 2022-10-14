from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        for i, num in enumerate(nums):
            if i == 0:
                sum_list.append(num)
                continue
            sum_list.append(sum_list[i-1] + nums[i])
            
        return sum_list
            