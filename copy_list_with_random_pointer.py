class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # time - O(n) space - O(n)
    def copyRandomList(self, head: Node) -> Node:
        oldToCopy = { None : None }
        cur = head

        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]