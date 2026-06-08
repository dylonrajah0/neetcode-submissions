class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqCount = {}
        maxCount = 0
        left = 0
        maxLen = 0
        for right, char in enumerate(s):
            print(char)
            freqCount[char] = freqCount.get(char,0)+1
            print(freqCount)
            maxCount = max(freqCount.values())
            print("max count", maxCount)
            windowSize = right - left + 1
            replacementsNeeded = windowSize - maxCount

            while replacementsNeeded > k:
                freqCount[s[left]] -= 1
                left += 1
                windowSize = right - left + 1
                maxCount = max(freqCount.values())
                replacementsNeeded = windowSize - maxCount

            maxLen = max(maxLen, windowSize)

            
        print(maxLen)
        return maxLen