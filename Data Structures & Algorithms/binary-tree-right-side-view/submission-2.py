# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        right = []

        def height(root: Optional[TreeNode], depth: int):

            if root is None:
                return

            if depth == len(right):
                right.append(root.val)

            height(root.right, depth + 1)
            height(root.left, depth + 1)

        height(root, 0)

        return right

