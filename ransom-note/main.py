class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note = {}
        for char in ransomNote:
            ransom_note[char] = 0
        for char in ransomNote:
            ransom_note[char] += 1
        
        magazine_ = {}
        for char in magazine:
            magazine_[char] = 0
        for char in magazine:
            magazine_[char] += 1
            
        for key in ransom_note:
            if ransom_note[key] > magazine_.get(key, 0):
                return False
        
        return True