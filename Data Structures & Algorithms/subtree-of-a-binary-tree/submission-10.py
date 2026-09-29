# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isTreeEqual(self, one, two):
        if not one and not two:
            return True
        if not one and two:
            return False
        if one and not two:
            return False
        
        if one.val != two.val:
            return False
        
        return self.isTreeEqual(one.left, two.left) and self.isTreeEqual(one.right, two.right) 
   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        
        if self.isTreeEqual(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        
