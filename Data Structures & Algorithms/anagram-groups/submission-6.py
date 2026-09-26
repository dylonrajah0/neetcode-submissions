class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         #Create a hashmap where the key is the character count and the word is a List
        #Start at beginning, take the word and get the frequency count. if it is not in the hashmap, add the character count as the key and value is empty List
        #then add the word in correct order to the List
        #Edge Cases: Empty strs. Store key as "" and list containing [""]
        #Runtime: O(n)

        hashmap = {}

        for word in strs:

            count = [0] * 26

            for char in word:
                count[ord(char) - 97] += 1

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []
                hashmap[key].append(word)
            else:
                hashmap[key].append(word)

        return list(hashmap.values())
