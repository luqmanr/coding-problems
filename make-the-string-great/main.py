class Solution:
    def makeGood(self, s: str) -> str:
        new_string = []
        final_string = ""
        for char in s:
            if len(new_string) == 0:
                new_string.append(char)
            elif ( char.isupper() and char.lower() == new_string[-1] or
                   char.islower() and char.upper() == new_string[-1] ):
                del new_string[-1]
            else:
                new_string.append(char)
        final_string = final_string.join(new_string)
        return final_string
