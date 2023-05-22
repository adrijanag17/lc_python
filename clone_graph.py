class Node:
    def __init__(self, val = 0, neighbors =  None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    # time - O(E+V) space - O()
    def clone_graph(self, node: Node) -> Node:
        
        # hashmap to map original nodes to cloned nodes
        old_to_new = {}

        # nested function - no need to pass the hashmap as argument
        def clone_dfs(node):

            if node in old_to_new:
                return old_to_new[node]
            
            clone = Node(node.val)
            old_to_new[node] = clone

            for n in node.neighbors:
                n_clone = clone_dfs(n)
                clone.neighbors.append(n_clone)
                
            return clone

        node_clone = clone_dfs(node)

        return node_clone if node else None


    