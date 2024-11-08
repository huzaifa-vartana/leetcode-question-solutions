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

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        if node.val in self.original_to_clone_mapping: return self.original_to_clone_mapping[node.val]
            
        self.original_to_clone_mapping[node.val] = Node(node.val)

        for neighbor in node.neighbors:
            self.original_to_clone_mapping[node.val].neighbors.append(self.cloneGraph(neighbor))


        return self.original_to_clone_mapping[node.val]


        