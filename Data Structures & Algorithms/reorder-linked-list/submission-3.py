# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = head

        count = 0

        while length != None:
            count += 1
            length = length.next

        mid = (count+1)//2

        secondList = head
        beforeSecond = None
        for i in range(mid):
            beforeSecond = secondList
            secondList = secondList.next

        beforeSecond.next = None
        firstList = head

        #reverse list 2

        
        prev = None
        curr = secondList
        next = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        #combine
        secondList = prev
        while secondList:
            temp1 = firstList.next
            temp2 = secondList.next

            firstList.next = secondList
            secondList.next = temp1

            firstList = temp1
            secondList = temp2


    

