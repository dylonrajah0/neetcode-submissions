class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:

        res = []

        start = 0

        while start < len(s):

            end = start

            while s[end] != '#':
                end += 1

            num = int(s[start:end])

            res.append(s[end+1: end+1+num])

            start = end + 1 + num

        return res