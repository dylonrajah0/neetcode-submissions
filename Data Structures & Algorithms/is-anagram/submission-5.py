class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charDict = {}

        for char in s:
            if char not in charDict:
                charDict[char] = 1

            else:
                charDict[char] += 1

        for char in t:
            if char not in charDict:
                return False
            else:
                charDict[char] -= 1

                if charDict[char] == 0:
                    charDict.pop(char)
        
        return not charDict