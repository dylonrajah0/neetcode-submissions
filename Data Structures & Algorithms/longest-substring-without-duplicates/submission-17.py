class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        length = 0
        alphaSet = set()


        while right < len(s):

            if s[right] in alphaSet:
                
                while s[right] in alphaSet:
                    alphaSet.remove(s[left])
                    left += 1

            alphaSet.add(s[right])
            
            length = max(length, len(alphaSet))
            right += 1
            length = max(length, len(alphaSet))
            

        return length