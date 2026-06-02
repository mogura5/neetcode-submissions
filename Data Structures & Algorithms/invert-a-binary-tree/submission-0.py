# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None

        eachLevel = [root]

        while eachLevel:
            parent = eachLevel.pop(0)

            temp = parent.left
            parent.left = parent.right
            parent.right = temp

            if parent.right:
                eachLevel.append(parent.right)
            if parent.left:
                eachLevel.append(parent.left)
            
        return root
            


        
        