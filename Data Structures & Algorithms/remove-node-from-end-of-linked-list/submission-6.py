# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        length = head

        count = 0

        while length != None:
            count += 1
            length = length.next

        if n == count:
            return head.next

        for i in range(count-n-1):
            slow = slow.next

        slow.next = slow.next.next

        return head


