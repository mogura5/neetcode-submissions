# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def depth(root):
            nonlocal ans

            if root is None:
                return 0
            
            leftTree = depth(root.left)
            rightTree = depth(root.right)

            which = max(leftTree, rightTree)

            ans = max(ans, which)

            return 1 + max(leftTree, rightTree)
        return depth(root)

       