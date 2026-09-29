class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        #1. freq count for substring

        s1Freq = [0]*26
        s1Length = len(s1)

        for char in s1:
            s1Freq[ord(char) - ord('a')] +=1

        left = 0

        while left <= len(s2) - s1Length:
            s1Copy = s1Freq.copy()
            charIndex = ord(s2[left]) - ord('a')

            if s1Freq[charIndex] > 0:
                #do something
                if self.checkWindow(left, left+s1Length, s1Copy, s2):
                    return True


            left+=1
        
        return False

    def checkWindow(self,left:int, right:int, s1Freq: List[int], s2:str) -> bool:

        while left < right:
            currChar = s2[left]
            charIdx = ord(currChar) - ord('a')
            if s1Freq[charIdx] > 0 and s1Freq[charIdx] != 0:
                s1Freq[charIdx] -= 1
            else:
                return False

            left +=1

        return sum(s1Freq) == 0