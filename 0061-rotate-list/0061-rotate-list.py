class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k %= length
        if k == 0:
            return head

        count = 1
        current = head
        while count < length - k:
            current = current.next
            count += 1

        new_head = current.next
        current.next = None
        tail.next = head

        return new_head
