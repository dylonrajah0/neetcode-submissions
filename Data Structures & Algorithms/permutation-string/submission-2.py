class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        

        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            s1Freq[index] += 1
        
        left = 0
        for right,char in enumerate(s2):
            
            

            if(right-left+1 > len(s1)):
                #window is full - move window
                #remove left
                s2Freq[ord(s2[left]) - ord('a')] -= 1
                #increment left
                left+=1
                #add right
                s2Freq[ord(char) - ord('a')] += 1
            
            else:
                index = ord(char)-ord('a')
                s2Freq[index] += 1

            
            if s1Freq == s2Freq:
                return True


        return False

