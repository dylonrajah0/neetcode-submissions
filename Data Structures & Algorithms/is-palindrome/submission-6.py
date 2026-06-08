class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        start = 0
        last = len(s) - 1

        if(len(s) == 1):
            return True

        


        while (start < last):
            

            while(start < last and not s[last].isalnum()):
                last-=1
            
            while(start < last and not s[start].isalnum()):
                start+=1

            if(start >= len(s) or last < 0):
                return False

            if(s[start] != s[last]):
                return False
            
            start+=1
            last-=1
        
        return True
        