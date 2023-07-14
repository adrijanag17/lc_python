class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:

    # time - O(n) space - O(1) where n = max(len(l1), len(l2))
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            cur.next = ListNode(value)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next