# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        answer = []

        queue.append(root)

        while queue:
            rightNode = None
            lenQueue = len(queue)

            for _ in range(lenQueue):

                lastNode = queue.pop(0)
                rightNode = lastNode

                if lastNode:
                    if lastNode.left:
                        queue.append(lastNode.left)
                    if lastNode.right:
                        queue.append(lastNode.right)
            if rightNode:
                answer.append(rightNode.val)
        
        return answer