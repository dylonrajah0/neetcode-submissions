class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a hashmap where the key is the word in sorted order and value is a List
        #Start at beginning, take the word and sort it. if it is not in the hashmap, add the sorted word as the key and value is empty List
        #then add the word in correct order to the List
        #Edge Cases: Empty strs. Store key as "" and list containing [""]
        #Runtime: O(n)

        hash = {}

        for word in strs:

            sortedWord = "".join(sorted(word))
            
            if sortedWord not in hash:
                hash[sortedWord] = []
                hash[sortedWord].append(word)
            else:
                hash[sortedWord].append(word)

        return list(hash.values())