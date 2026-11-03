class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        right = 0
        maxNum = 0

        while right < len(s):

            if s[right] in charset:
                maxNum = max(maxNum,len(charset))
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1

            charset.add(s[right])
            maxNum = max(maxNum,len(charset))
            right += 1

        return maxNum