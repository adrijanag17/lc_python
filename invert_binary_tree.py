class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n) space - O(h) or O(n) where h is the height of tree
    def invert_tree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None
        
        right, left = root.right, root.left
        root.left, root.right = right, left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root
    

    # alternatively
    def invert(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.invert(root.left)
        right = self.invert(root.right)

        root.left = right
        root.right = left

        return root