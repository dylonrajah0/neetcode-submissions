class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        start = 0
        last = len(s)-1

        while(start < last):

            if start < last and not s[start].isalnum():
                start +=1
            elif start < last and not s[last].isalnum():
                last -=1
            else:
                if s[start] != s[last]:
                    return False
                
                start+=1
                last -=1
        return True