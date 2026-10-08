class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        print(res)
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        index = 0

        while index < len(s):

            numString = ""
            while s[index] != "#":
                numString += s[index]
                index += 1

            print(numString)
            print(len(numString))
            num = int(numString)

            word = s[index+1 : index + num +1]
            res.append(word)
            print(word)

            index = index + 1 + num

        print(res)
        return res