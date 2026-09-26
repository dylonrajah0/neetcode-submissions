# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        self.inOrder(root, res)

        for i in res:
            print(i)


        return res[k-1]

    def inOrder(self, node: Optional[TreeNode], res: List[int]):
        if node is None:
            return

        # Traverse the left subtree first
        self.inOrder(node.left, res)

        # Visit the current node
        res.append(node.val)

        # Traverse the right subtree last
        self.inOrder(node.right, res)