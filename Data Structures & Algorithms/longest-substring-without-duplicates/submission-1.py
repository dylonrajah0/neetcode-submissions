class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()
        currMax = 0
        left = 0

        for right, value in enumerate(s):

            while value in hashset:
                hashset.remove(s[left])
                left+=1

            
            hashset.add(value)
            currMax = max(currMax, right-left+1)

        return currMax