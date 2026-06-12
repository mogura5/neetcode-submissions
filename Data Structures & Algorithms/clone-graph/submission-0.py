"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #hashmap to map old to new node
        oldToNew = {}

        def dfs(node):

            if node in oldToNew:
                # we already made a clone of it
                return oldToNew[node]
            if node is None:
                return None
            newNode = Node(node.val)
            oldToNew[node] = newNode

            # make copies of neighbors
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))
            return newNode
        return dfs(node)

       




        