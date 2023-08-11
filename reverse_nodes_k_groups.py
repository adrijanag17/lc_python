class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # time - O(n) space - O(1)
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        kth = self.getKth(groupPrev, k)

        while kth:
            groupNext = kth.next
            # reverse the group
            cur, prev = groupPrev.next, groupNext
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp

            kth = self.getKth(groupPrev, k)

        return dummy.next



    def getKth(self, cur, k):

        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur