class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        new_word = ""
        found = -1
        for i, char in enumerate(word):
            if char == ch:
                found = i
                break
        if found == -1:
            return word
        
        first_half = word[:found+1]
        for char in first_half[::-1]:
            new_word += char
        
        new_word = new_word + word[found+1:]
        
        return new_word