class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = 0
        maxArea = 0

        while(right < len(height)):

            if right+1 < len(height) and height[right] > height[right+1]:
                left = right
                currArea = 0
                maxRightIndex = -1
                right += 1

                while right < len(height) and height[right] < height[left]:
                    currArea -= height[right]
                    

                    if maxRightIndex == -1 or height[right] > height[maxRightIndex]:
                        maxRightIndex = right
                    
                    right += 1

                if right == len(height):
                    if maxRightIndex == -1:
                        return maxArea

                    right = maxRightIndex
                    currArea = -sum(height[left+1:right])

                currArea += ((right - left)-1) * min(height[right], height[left])
                maxArea += currArea
                left = right
            else:
                right += 1

        return maxArea
            

            