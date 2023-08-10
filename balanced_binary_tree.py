class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(n)
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node):

            if not node:
                return [True, 0]
            
            left, right = dfs(node.left), dfs(node.right)

            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <=1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]


    def isBalanced2(self, root: TreeNode) -> bool:

        diff = 0
        def dfs(node):
            nonlocal diff

            if not node:
                return 0

            leftDepth, rightDepth = dfs(node.left) + 1, dfs(node.right) + 1

            diff = max(diff, abs(leftDepth - rightDepth))

            return max(leftDepth, rightDepth)

        dfs(root)

        return True if diff <= 1 else False

            
