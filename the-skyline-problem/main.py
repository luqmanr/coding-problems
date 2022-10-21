class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        chars = set(s)
        counts = []
        for char in chars:
            count = [z for z in s if z == char]
            counts.append(len(count))
        counts = set(counts)
        if len(counts) > 1:
            return False
        return True