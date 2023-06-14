class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Codec:

    # time - O(n) space - O(h) = O(n)
    def serialize(self, root: TreeNode) -> str:
        res = []

        # preorder dfs
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    
    # time - O(n) space - O(n)
    def deserialize(self, data: str) -> TreeNode:

        vals = data.split(",")
        
        # can use i = [0] or nonlocal i instead as well for global variable declaration of i
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

