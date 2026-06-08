class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #strat: increment right pointer and add everything to set
        #once we find the duplicate, remove from the left side until the duplicate is
        #removed. calculate max and move on

        alphaSet = set()
        left = 0
        maxVal = 0
        for right, value in enumerate(s):
            print("right", right)
            print("value", value)

            if value in alphaSet:
                print("need to remove")
                maxVal = max(maxVal, len(alphaSet))
                while value in alphaSet:
                    print("going to remove: ", s[left])
                    alphaSet.remove(s[left])
                    print(alphaSet)
                    left+=1


            alphaSet.add(value)
            maxVal = max(maxVal, len(alphaSet))
            print(alphaSet)
            print("Max Size: ", maxVal)

        return maxVal