class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(n) - call stack in worst case scenario
    def max_depth(self, root: TreeNode) -> int:
        # DFS
        def dfs(root):

            if not root:
                return 0

            left_depth = right_depth = 0

            left_depth += dfs(root.left)
            right_depth += dfs(root.right)

            depth = 1 + max(left_depth, right_depth)
            
            return depth

        return dfs(root)

    
    # concise version
    def max_depth2(self, root: TreeNode) -> int:

        if not root:
            return 0

        left_depth = right_depth = 0
        left_depth += self.max_depth(root.left)
        right_depth += self.max_depth(root.right)

        return (1 + max(left_depth, right_depth))


