# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        hed = dummy

        dct = {}
        
        while hed.next and hed.next.next:
            if hed.next.val == hed.next.next.val:
                dct[hed.next.val] = 1
                while hed.next and hed.next.next and hed.next.val == hed.next.next.val:
                    hed.next = hed.next.next
                hed.next = hed.next.next
            else:
                hed = hed.next
            
        return dummy.next
