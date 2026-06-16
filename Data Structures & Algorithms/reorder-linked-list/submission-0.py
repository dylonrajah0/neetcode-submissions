# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        values = []

        dummy = head

        while dummy != None:
            values.append(dummy.val)
            dummy = dummy.next

        print(values)

        start = 0
        end = len(values)-1

        reorderedList = []
        while start <= end:
            reorderedList.append(values[start])
            reorderedList.append(values[end])
            start += 1
            end -= 1
            
        dummy = head
        i = 0

        while dummy:
            dummy.val = reorderedList[i]
            dummy = dummy.next
            i += 1
        #while still != None:
            #print(still.val)
            #still = still.next


        return None