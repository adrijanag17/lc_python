class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    # remove node from current position is list
    def _remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode


    # insert node to the end of the list
    def _insert(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:

        if key in self.map:
            self._remove(self.map[key])
            self._insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])

        newNode = ListNode(key, value)
        self.map[key] = newNode
        self._insert(newNode)

        if len(self.map) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)