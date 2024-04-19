# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next_node = None
        
        # Traverse the list and reverse pointers
        while curr:
            # Store the next node
            next_node = curr.next
            
            # Reverse the current node's pointer
            curr.next = prev
            
            # Move prev and curr pointers one step forward
            prev = curr
            curr = next_node
        
        # Return the new head of the reversed list
        return prev