# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        
        # Track visited levels to ensure only one node per level
        visited_levels = set()
        
        def recurse(node, right_node, level):
            nonlocal res, visited_levels
            if not node: return

            # Only add a node if there's no node to its right AND we haven't added a node at this level yet
            if not right_node and level not in visited_levels:
                res.append(node.val)
                visited_levels.add(level)
                
            right_ptr, left_ptr = None, None
            if right_node:
                right_ptr = right_node.left or right_node.right
            
            left_ptr = node.right or right_ptr

            recurse(node.right, right_ptr, level + 1)
            recurse(node.left, left_ptr, level + 1)

        recurse(root, None, 0)
        return res
