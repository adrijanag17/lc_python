class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # time - O(mn) space - O(m+n)
    def is_subtree(self, root: TreeNode, subroot: TreeNode) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        if self.same_tree(root, subroot):
            return True
        
        return (self.is_subtree(root.left, subroot) or
                self.is_subtree(root.right, subroot))


    def same_tree(self, p, q):

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        
        return (self.same_tree(p.left, q.left) and
                self.same_tree(p.right, q.right))
         