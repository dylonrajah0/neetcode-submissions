# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None

        while(curr != None):
            
            #keep pointer to next
            next = curr.next

            #change pointer to previous
            curr.next = prev

            #move everything up
            prev = curr
            curr = next
            

        return prev