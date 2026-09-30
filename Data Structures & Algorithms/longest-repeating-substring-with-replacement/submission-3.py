class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}

        left = 0
        right = 0
        maxLength = -10

        while right < len(s):

            currChar = s[right]

            if currChar not in seen:
                seen[currChar] = 1
            else:
                seen[currChar] += 1

            if (right - left +1) - max(seen.values()) > k:
                while (right - left +1) - max(seen.values()) > k:
                    seen[s[left]] -= 1
                    left += 1

                
            
            maxLength = max(maxLength, right-left+1)
            right+=1
        
      
        return maxLength

