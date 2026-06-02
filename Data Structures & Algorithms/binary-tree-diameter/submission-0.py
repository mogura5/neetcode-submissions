# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        def height(root):
            nonlocal diameter
            if root is None:
                return 0

            leftTree = height(root.left)
            rightTree = height(root.right)

            diameter = max(diameter, leftTree + rightTree)
            
            return 1 + max(leftTree, rightTree)
        
        height(root)

        return diameter
            
            