class ListNode:
    def __init__(self, val=0, next=None):
        this.val = val
        this.next = next

class Solution:

    # iterative
    # time - O(n) space - O(1)
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    
    # time - O(n) space - O(n)
    def reverse_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return _reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev

        nxt = node.next
        node.next = prev
        return _reverse(nxt, node)
