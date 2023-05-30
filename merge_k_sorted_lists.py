class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # time - O(nklogk) space - O(1)
    def merge_k_lists(self, lists: list[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:           # will run logk times - O(logk)
            merged_lists = []

            for i in range(0, len(lists), 2):       # will run k/2 times - O(k)
                list1 = lists[i]
                list2 = lists[i+1] if (i + 1) < len(lists) else None

                merged_lists.append(self.merge(list1, list2))       # each call to merge - O(n)

            lists = merged_lists

        return lists[0]


    # time - O(n) space - O(1)
    def merge(self, list1, list2):

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next
