# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0


        l1Pointer = l1
        l2Pointer = l2

        dummy = ListNode(0)
        curr = dummy
        

        while l1Pointer != None and l2Pointer != None:
            num = l1Pointer.val + l2Pointer.val + carry
            
            curr.next = ListNode(num % 10)
            curr = curr.next

            carry = num // 10

            l1Pointer = l1Pointer.next
            l2Pointer = l2Pointer.next

        # get remaining nodes of l2. cause the above loop will keep the rest of l1

        while l1Pointer != None:
            num = l1Pointer.val + carry 
            carry = num//10
            curr.next = ListNode(num %10)
            curr = curr.next
            l1Pointer = l1Pointer.next




        while l2Pointer != None:
            
            num = l2Pointer.val + carry 
            carry = num //10
            curr.next = ListNode(num % 10)
            curr = curr.next
            l2Pointer = l2Pointer.next



        #add the last carry value
        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next
            

