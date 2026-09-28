class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        #Find the shortest word
        smallest = strs[0]

        for word in strs:
            
            if len(word) < len(smallest):
                smallest = word
        
        #Loop smallest word and compare to the rest of them

        res = ""

        for smallIndex in range(0, len(smallest)):

            for word in strs:

                if smallest[smallIndex] != word[smallIndex]:
                    return res
            
            res += smallest[smallIndex]
        
        return res