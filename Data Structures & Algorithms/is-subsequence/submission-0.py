class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
     sPointer = 0
    

     for tPointer in range(len(t)):
        if sPointer == len(s):
                return True

        if t[tPointer] == s[sPointer]:
            sPointer = sPointer + 1


    
     return sPointer == len(s)
