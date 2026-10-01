class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1FreqCount = [0]*26

        
        for char in s1:
            s1FreqCount[ord(char) - ord('a')] += 1
        
        left = 0
        right = 0
        compareFreq = [0] * 26

        while right < len(s2):
            currChar = s2[right]

            compareFreq[ord(currChar) - ord('a')] += 1

            if right - left + 1 > len(s1):
                compareFreq[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if right - left + 1 == len(s1):
                if compareFreq == s1FreqCount:
                    return True

            right += 1
        return False

