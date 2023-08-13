class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(n/2) = O(n)
    def goodNodes(self, root: TreeNode) -> int:

        count = 0
        def dfs(node, max):
            nonlocal count
            if not node:
                return
            
            if node.val >= max:
                count += 1
                max = node.val

            dfs(node.left, max)
            dfs(node.right, max)

        dfs(root, root.val)
        return count