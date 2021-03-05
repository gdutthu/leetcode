# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        arr = []
        queue = [root]
        while len(queue) > 0:
            nextNode = []
            curMax = float("-inf")
            for node in queue:
                if node.val > curMax:
                    curMax = node.val

                if node.left != None:
                    nextNode.append(node.left)
                if node.right != None:
                    nextNode.append(node.right)
            arr.append(curMax)
            if len(nextNode) > 0:
                queue = nextNode
            else:
                break
        return arr