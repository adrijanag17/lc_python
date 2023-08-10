class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(n)
    def diameter(self, root: TreeNode) -> int:

        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return -1
            
            leftHeight, rightHeight = dfs(node.left), dfs(node.right)
            res = max(res, leftHeight + rightHeight + 2)

            return max(leftHeight, rightHeight) + 1
        
        dfs(root)

        return res