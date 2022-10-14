from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        messages = []
        for i in range(n+1):
            if i == 0:
                continue
            elif i % 3 == 0 and i % 5 == 0:
                messages.append("FizzBuzz")
            elif i % 3 == 0:
                messages.append("Fizz")
            elif i % 5 == 0:
                messages.append("Buzz")
            else:
                messages.append(str(i))
        return messages
