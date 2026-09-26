class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #initialize left and right of window at beginning
        #add right values to hashset
        #if its not unique, save window size, keep looking
        #move left to right+1
        #base Case: If string is empty, return 0. If string is len 1, return 1

        hash = set()

        if len(s) < 2:
            return len(s)

        left = 0
        right = 0
        maxWindow = 0

        while right < len(s):
            if s[right] in hash:
                while s[right] in hash:
                    hash.remove(s[left])
                    left += 1

                
            hash.add(s[right])
            maxWindow = max(maxWindow, right-left+1)
            right += 1

        
        return maxWindow
