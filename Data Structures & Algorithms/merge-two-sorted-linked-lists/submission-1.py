# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1pointer = list1
        l2pointer = list2

        if not list1:
            return list2

        if not list2:
            return list1

        if l1pointer.val < l2pointer.val:
            head = l1pointer
            l1pointer = l1pointer.next
        else:
            head = l2pointer
            l2pointer = l2pointer.next

        start = head

        while l1pointer and l2pointer is not None:

            if l1pointer.val < l2pointer.val:
                head.next = l1pointer
                head = head.next
                l1pointer = l1pointer.next
            else:
                head.next = l2pointer
                head = head.next
                l2pointer = l2pointer.next

        
        while l1pointer is not None:
            head.next = l1pointer

            head = head.next
            l1pointer = l1pointer.next

        while l2pointer is not None:
            head.next = l2pointer

            head = head.next
            l2pointer = l2pointer.next

        return start


        