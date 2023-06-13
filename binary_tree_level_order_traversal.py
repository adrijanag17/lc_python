import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(n/2) = O(n) not counting result list
    def level_order(self, root: TreeNode) -> list[list[int]]:

        if not root:
            return []
        
        res = []
        q = collections.deque([root])

        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node)

            res.append(level)

        return res