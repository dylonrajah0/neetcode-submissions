class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        setS = {}

        for i in s:
            print(i)
            setS[i] = setS.get(i,0) + 1


        setT ={}
        for i in t:
            print(i)
            setT[i] = setT.get(i,0) + 1

        if setS == setT:
            return True
        else:
            return False