class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def solve(node):
            if not node: return None

            left, right = solve(node.left), solve(node.right)
            if node == p or node == q: return node
            if left and right: return node
            if left: return left
            if right: return right
            return None



        return solve(root)