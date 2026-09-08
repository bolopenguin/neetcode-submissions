# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def depth(node):
            if not node:
                return 0
            
            return 1 + max(depth(node.left), depth(node.right))
        
        is_balanced = abs(depth(root.left) - depth(root.right)) <= 1
        print(is_balanced)
        print( abs(depth(root.left) - depth(root.right)))
        return is_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)