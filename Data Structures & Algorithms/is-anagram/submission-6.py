class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charDict = [0] * 26

        for char in s:
           charDict[ord(char) - ord('a')] += 1

        for char in t:
            charDict[ord(char) - ord('a')] -= 1
        
        return all(x == 0 for x in charDict)