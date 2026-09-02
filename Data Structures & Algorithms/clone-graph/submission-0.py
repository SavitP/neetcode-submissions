"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
            m = {}
            done = set()

            if node is None:
                return None
            def create(n):
                if n.val not in m:
                    m[n.val] = Node(n.val)
                done.add(n.val)
                for neighbor in n.neighbors:
                    if neighbor.val not in m:
                        m[neighbor.val] = Node(neighbor.val)
                    m[n.val].neighbors.append(m[neighbor.val])
                    if neighbor.val not in done:
                        create(neighbor)

            create(node)
            return m[node.val]