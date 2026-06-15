# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return None


        length = head
        count = 0
        while length != None:
            count += 1
            length = length.next

        print("Length: ", count)

        if n == count:
            return head.next
        
        dummy = head
        for i in range(count-n-1):
            print("Current position: ", dummy.val)
            dummy = dummy.next
            print(i)

        dummy.next = dummy.next.next


        print("Ending position: ", dummy.val)
        return head