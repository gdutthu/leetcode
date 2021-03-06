# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        right_arr=[]
        queue=[root]
        while len(queue)>0:
            nextNode=[]
            curNode=[]
            for node in queue:
                curNode.append(node.val)
                if node.left !=None:
                    nextNode.append(node.left)
                if node.right !=None:
                    nextNode.append(node.right)
            right_arr.append(curNode[-1])
            if len(nextNode)>0:
                queue=nextNode
            else:
                break
        return right_arr