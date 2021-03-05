# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        arr=[]
        queue=[root]
        while len(queue)>0:
            count=0
            nextNode=[]
            for node in queue:
                count +=node.val
                if node.left!=None:
                    nextNode.append(node.left)
                if node.right!=None:
                    nextNode.append(node.right)
            arr.append(count/len(queue))
            if len(nextNode)>0:
                queue=nextNode
            else:
                break
        return arr