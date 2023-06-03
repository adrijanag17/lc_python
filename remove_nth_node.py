class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # time - O(n) space - O(1)
    def remove_nth_node(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next