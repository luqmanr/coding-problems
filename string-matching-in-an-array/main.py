class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for to_find in words:
            for to_match in words:
                if to_find in to_match and to_find != to_match:
                    substrings.append(to_find)

        return set(substrings)