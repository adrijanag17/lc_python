class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(n)
    def kth_smallest(self, root: TreeNode, k: int) -> int:

        inorder = []

        # perform recursive inorder traversal
        def inorder_dfs(node):
            if not node:
                return
            
            if node.left:
                inorder_dfs(node.left)
            inorder.append(node.val)
            if node.right:
                inorder_dfs(node.right)

        inorder_dfs(root)
        return inorder[k-1]

    
    # alternatively - without the additional list space
    def kth(self, root: TreeNode, k: int) -> int:
        n, val = 0, float("inf")

        def dfs(node):
            nonlocal n, val
            if not node:
                return
            
            if node.left:
                dfs(node.left)
            if n != k:
                n += 1
            else:
                return
            if n == k:
                val = node.val
                return
            if node.right:
                dfs(node.right)

        dfs(root)
        return val
            