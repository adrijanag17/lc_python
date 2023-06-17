class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recursive: time - O(h) space - O(h) where h is the height of the bst
    def lowest_commone_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < root.val and q.val < root.val:
            return self.lowest_commone_ancestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowest_commone_ancestor(root.right, p, q)
        
        return root


    # iterative: time - O(h) space - O(1)
    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur