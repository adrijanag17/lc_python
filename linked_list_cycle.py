class ListNode:
    def __init__(self, val=0, next=None):
        this.val = val
        this.next = next


class Solution:
    # time - O(n) space - O(1)
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False