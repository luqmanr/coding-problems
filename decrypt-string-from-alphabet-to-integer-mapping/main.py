class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = "+abcdefghijklmnopqrstuvwxyz"
        keys = {}
        for i in range(len(letters)):
            keys[str(i)] = letters[i]
        letters_found = []
        for i,c in enumerate(s):
            if c == "#":
                num = s[i-2] + s[i-1]
                del letters_found[-1]
                del letters_found[-1]
                letters_found.append(keys[num])
            else:
                letters_found.append(keys[c])
        return ''.join(letters_found)
            