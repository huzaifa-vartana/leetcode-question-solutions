"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.original_to_clone_mapping = {}

    def dfs(self, node):
            
        self.original_to_clone_mapping[node.val] = Node(node.val)
        for neighbor in node.neighbors:
            if neighbor.val not in self.original_to_clone_mapping:
                self.dfs(neighbor)

            self.original_to_clone_mapping[node.val].neighbors.append(self.original_to_clone_mapping[neighbor.val])




    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        self.dfs(node)


        return self.original_to_clone_mapping[node.val]





        