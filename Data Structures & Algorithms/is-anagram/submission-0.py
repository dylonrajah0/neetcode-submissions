class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        setS = {}

        for i in s:
            print(i)
            if i not in setS:
                setS[i] = 0

            setS[i] = setS.get(i) + 1


        setT ={}
        for i in t:
            print(i)
            if i not in setT:
                setT[i] = 0

            setT[i] = setT.get(i) + 1

        if setS == setT:
            return True
        else:
            return False