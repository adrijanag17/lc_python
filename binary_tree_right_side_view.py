import collections
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(1)
    def rightSideView(self, root: TreeNode) -> list[int]:

        if not root:
            return []
        
        # using bfs
        res = []
        q = collections.deque([root])
        while q:
            rightMost = None

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                rightMost = node

            res.append(rightMost.val)
        return res