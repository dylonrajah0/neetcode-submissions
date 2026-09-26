# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Initialize a queue as the data structure
        #Begin by adding the root
        #Loop the size of the queue
        #In the loop, Add the children
        #then remove from the front and save to List

        if root is None:
            return []

        result = []

        queue = deque()

        queue.append(root)

        while queue:
            levelList = []
            for i in range(len(queue)):
                
                currNode = queue.popleft()
                levelList.append(currNode.val)

                if currNode.left != None:
                    queue.append(currNode.left)
                
                if currNode.right != None:
                    queue.append(currNode.right)

            result.append(levelList)
        
        return result

            


        