# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = None
        while l1:
            next_node = l1.next
            l1.next = prev1
            prev1 = l1
            l1 = next_node
        
        prev2 = None
        while l2:
            next_node = l2.next
            l2.next = prev2
            prev2 = l2
            l2 = next_node
        
        curr1, curr2 = prev1, prev2
        dummy = ListNode()  
        curr = dummy
        carry = 0
        
        while curr1 or curr2 or carry:
            sum_val = carry
            if curr1:
                sum_val += curr1.val
                curr1 = curr1.next
            if curr2:
                sum_val += curr2.val
                curr2 = curr2.next
            
            carry, val = divmod(sum_val, 10)
            
            curr.next = ListNode(val)
            curr = curr.next
        
        prev = None
        curr = dummy.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev