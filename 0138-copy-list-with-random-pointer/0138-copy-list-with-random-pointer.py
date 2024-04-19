"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dct={}
        curr=head
        while curr:
            dct[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            dct[curr].next=dct.get(curr.next)
            dct[curr].random=dct.get(curr.random)
            curr=curr.next
            
        return dct[head]