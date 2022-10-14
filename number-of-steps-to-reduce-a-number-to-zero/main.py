class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            remainder = num % 2
            if remainder == 0:
                num = num / 2
            elif num == 1:
                num = 0
            else:
                num = num - 1
            counter += 1
        
        return counter