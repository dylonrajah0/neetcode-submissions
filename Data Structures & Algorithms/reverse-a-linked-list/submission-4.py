# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        if not curr:
            return None
            
        prev = None
        next = curr.next

        while next != None:

            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        
        curr.next = prev
        prev = curr

        return prev