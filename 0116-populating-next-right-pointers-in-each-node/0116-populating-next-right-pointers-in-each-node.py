"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':


        def recurse(node):
            if not node: return
            if node.left:
                if node.right:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = node.next.left
            recurse(node.left)
            recurse(node.right)

        recurse(root)

        return root

        