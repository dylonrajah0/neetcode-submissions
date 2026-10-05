class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:
            freqCount = [0] * 26

            for char in word:
                freqCount[ord(char) - ord('a')] += 1

            key = tuple(freqCount)

            if key not in hashmap:
                hashmap[key] = []
                hashmap[key].append(word)
            else:
                hashmap[key].append(word)

        return list(hashmap.values())        