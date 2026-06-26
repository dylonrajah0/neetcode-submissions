# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.maxSoFar(root, -1000)
    

    def maxSoFar(self, root: TreeNode, maxNum: int) -> int:

        if not root:
            return 0


        good = 0

        if root.val >= maxNum:
            good = 1

        maxNum = max(root.val, maxNum)

        return good + self.maxSoFar(root.left, maxNum) + self.maxSoFar(root.right, maxNum)