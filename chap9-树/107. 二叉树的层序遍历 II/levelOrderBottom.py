# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        result=[]
        queue=[root]
        while len(queue)>0:
            cur=[]
            nextNode=[]
            for node in queue:
                cur.append(node.val)
                if node.left!=None:
                    nextNode.append(node.left)
                if node.right !=None:
                    nextNode.append(node.right)
            result.append(cur)
            if len(nextNode)>0:
                queue=nextNode
            else:
                break
        left=0
        right=len(result)-1
        while left<right:
            result[left],result[right]=result[right],result[left]
            left +=1
            right -=1
        return result