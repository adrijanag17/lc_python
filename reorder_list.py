class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    
    # time - O(n) space - O(1)
    def reorder_list(self, head: ListNode) -> None:

        # find middle point of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        # reverse second half
        prev, curr = None, right
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        left, right = head, prev

        # merge two halves
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left, right = tmp1, tmp2
