class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1length = len(s1)
        s1Freq = [0]*26

        compareFreq = [0]*26

        for char in s1:
            s1Freq[ord(char) - ord('a')] += 1

        left = 0
        right = 0

        while right < len(s2):

            char = s2[right]
            charIndex = ord(char) - ord('a')
            compareFreq[charIndex] += 1

            if right - left + 1 > s1length:
                charLeft = s2[left]
                charIdxLeft = ord(charLeft) - ord('a')
                compareFreq[charIdxLeft] -= 1
                left +=1

            if right - left + 1 == s1length:
                if s1Freq == compareFreq:
                    return True

            right += 1

        return False










