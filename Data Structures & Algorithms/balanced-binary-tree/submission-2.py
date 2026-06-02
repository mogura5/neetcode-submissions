# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        search = []
        def dfs(root):

            if root is None:
                return [True, 0]

            leftTree = dfs(root.left)
            rightTree = dfs(root.right)
            height = max(rightTree[1], leftTree[1])

            if not leftTree[0] or not rightTree[0] or abs(rightTree[1] - leftTree[1]) > 1:
                isBalanced = False
            else:
                isBalanced = True
            
            return [isBalanced, height + 1]

        return dfs(root)[0]
