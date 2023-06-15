class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # time - O(n^2) space - O()
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.build_tree(preorder[1:mid+1], inorder[:mid])
        root.right = self.build_tree(preorder[mid+1:], inorder[mid+1:])

        return root