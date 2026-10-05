class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False


        freqCount = [0] * 26
        for char in s1:
            freqCount[ord(char) - ord('a')] += 1

        left = 0
        right = 0
        countFreq = [0] * 26

        while right < len(s2):

            countFreq[ord(s2[right]) - ord('a')] += 1

             # Shrink if window is too large
            if right - left + 1 > len(s1):
                countFreq[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # Check if current window is a permutation
            if right - left + 1 == len(s1):
                if countFreq == freqCount:
                    return True

            right += 1

        return False




