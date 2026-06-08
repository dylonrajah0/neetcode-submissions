class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        

        s1Freq = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            s1Freq[index] += 1
        
        
        left = 0
        right = len(s1)
        print("Right:", right)

        while right <= len(s2):
            window = s2[left:right]
            s2Freq = [0] * 26
            print("Window: ", window)
            for char in window:
                index = ord(char)-ord('a')
                s2Freq[index] += 1

            print("Freq2: ", s2Freq)
            if s1Freq == s2Freq:
                return True

            left +=1
            right += 1

        return False

