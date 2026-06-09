class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #If there is just one element, return the element
        #in a new List

        wordMap = {}

        for word in strs:
            #print("Word: ", word)
            sortedWord = "".join(sorted(word))
            #print("Sorted Word: ", sortedWord)
            if sortedWord not in wordMap:
                wordMap[sortedWord] = []

            wordMap[sortedWord].append(word)



        res = []

        for key in wordMap:
            #print(wordMap[key])
            res.append(wordMap[key])


        #print(res)
        return res

        