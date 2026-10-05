class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        hashset = set()
        maxWindow = 0

        while right < len(s):

            if s[right] in hashset:
                while s[right] in hashset:
                    hashset.remove(s[left])
                    left+= 1

            hashset.add(s[right])
            maxWindow = max(maxWindow, right -left +1)
            right +=1

        return maxWindow
 