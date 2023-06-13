class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(h)
    def max_path_sum(self, root: TreeNode) -> int:

        # nonlocal variable
        sum = root.val

        # function that returns max sum if no splitting is allowed
        def sum_dfs(node):
            nonlocal sum

            if not node:
                return 0
            
            # max of val and 0 - if there are negative values
            left_sum = max(sum_dfs(node.left), 0)
            right_sum = max(sum_dfs(node.right), 0)

            sum = max(sum, left_sum + right_sum + node.val)

            return node.val + max(left_sum, right_sum)
        
        sum_dfs(root)
        return sum