class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num = max(nums) - k
        min_num = min(nums) + k
        
        score = max_num - min_num
        if score < 0:
            return 0
        return score
        