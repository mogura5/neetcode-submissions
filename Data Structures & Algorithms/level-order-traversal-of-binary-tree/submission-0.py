# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levelQueue = []
        result = []
        levelQueue.append(root)

        while levelQueue:
            qLen = len(levelQueue)
            level = []

            for _ in range(qLen):
                node = levelQueue.pop(0)

                if node:
                    level.append(node.val)
                    levelQueue.append(node.left)
                    levelQueue.append(node.right)

            if level:
                result.append(level)
        return result