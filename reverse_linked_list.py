class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # iterative
    # time - O(n) space - O(1)
    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    
    # time - O(n) space - O(n)
    def reverse_recursive(self, head: ListNode) -> ListNode:
        return self.reverse(head)

    def reverse1(self, node, prev=None):
        if not node:
            return prev

        nxt = node.next
        node.next = prev
        return self.reverse(nxt, node)
