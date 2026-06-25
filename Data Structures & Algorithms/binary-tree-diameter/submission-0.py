# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is the longest path from any two nodes
        self.res = 0
        # get the height of each node

        self.height(root)

        return self.res


    def height(self, root: Optional[TreeNode]):

        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        self.res = max(self.res, left+right)

        return 1 + max(left, right)