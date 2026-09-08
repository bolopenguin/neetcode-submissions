# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def node_depth(root):
            if not root:
                return 0
            
            return 1 + max(node_depth(root.left), node_depth(root.right))

        
        
        diameter = node_depth(root.left) + node_depth(root.right)

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(diameter, max(left_diameter, right_diameter))