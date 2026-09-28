class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charDict = {}

        for i in range(0, len(s)):
             
             if s[i] in charDict:
                charDict[s[i]] += 1
             else:
                charDict[s[i]] = 1

        for j in range(0, len(t)):

            if t[j] in charDict:
                charDict[t[j]] -= 1

                if charDict[t[j]] == 0:
                    charDict.pop(t[j])

            else:
                return False

        return not charDict