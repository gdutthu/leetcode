# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue=[root]
        while len(queue)>0:
            nextNode=[]
            leftVal=queue[0].val
            for node in queue:
                if node.left !=None:
                    nextNode.append(node.left)
                if node.right!=None:
                    nextNode.append(node.right)
            if len(nextNode)>0:
                queue=nextNode
            else:
                return leftVal