# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        multiplier = 1

        l1Point = l1
        l2Point = l2

        l1Value = 0
        l2Value = 0

        while l1Point is not None:
            l1Value += l1Point.val * multiplier
            l1Point = l1Point.next
            multiplier *= 10

        multiplier = 1

        while l2Point is not None:
            l2Value += l2Point.val * multiplier
            l2Point = l2Point.next
            multiplier *= 10

        print(l1Value)
        print(l2Value)
        sumVal = l1Value + l2Value
        print(sumVal)

        if sumVal == 0:
            return ListNode(0)

        res = ListNode()
        curr = res

        while sumVal > 0:
            curr.next = ListNode(sumVal % 10)
            curr = curr.next
            sumVal = sumVal // 10

        return res.next
