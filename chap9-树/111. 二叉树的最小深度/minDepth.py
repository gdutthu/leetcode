# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        minLevel = 1
        queue = [root]
        while len(queue) > 0:
            nextNode = []
            for node in queue:
                if node.left == None and node.right == None:
                    return minLevel

                if node.left != None:
                    nextNode.append(node.left)
                if node.right != None:
                    nextNode.append(node.right)

            if len(nextNode) > 0:
                queue = nextNode
            else:
                return minLevel
            minLevel += 1