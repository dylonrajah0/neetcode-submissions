# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #initialize a queue and list to hold all lists

        # add root to queue

        #while the loop is not empty
            #create a new list representing the level
            #calculate the size of queue
            #loop the size of the queue
            #take out elements and add them to level list (check for null/none)
            #add the children to queue
            #once loop ends, add to list of lists

            res = []

            q = deque()

            q.append(root)

            while q:
                level = []

                for i in range(len(q)):
                    
                    node = q.popleft()

                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)

                if level:
                    res.append(level)


            return res
























