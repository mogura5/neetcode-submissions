# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0

        def dfs(node, maxNode):

            if node is None:
                return 0

            if node.val >= maxNode:
                output = 1
            else:
                output = 0

            maxNode = max(maxNode, node.val)
            output += dfs(node.left, maxNode)
            output += dfs(node.right, maxNode)

            return output

        return dfs(root, root.val)