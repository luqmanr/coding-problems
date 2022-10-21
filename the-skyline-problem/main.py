class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        chars = []
        for char in s:
            chars.append(char)
        chars = set(chars)
        counts = []
        for char in chars:
            count = 0
            for z in s:
                if z == char:
                    count += 1
            counts.append(count)
        counts = set(counts)
        if len(counts) > 1:
            return False
        return True