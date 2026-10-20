class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:

            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:

        words = []
        i = 0
        while i < len(s):


            stringNum = ""

            while s[i] != "#":
                stringNum += s[i]
                i += 1
            
            num = int(stringNum)
            i+= 1
            words.append(s[i:i+num])

            i += num

        return words

