# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        result=[]
        level=0
        queue=[root]
        while len(queue)>0:
            level +=1
            cur=[]
            nextNode=[]
            for node in queue:
                cur.append(node.val)
                if node.left!=None:
                    nextNode.append(node.left)
                if node.right!=None:
                    nextNode.append(node.right)

            if level%2==0:
                left=0
                right=len(cur)-1
                while left<right:
                    cur[left],cur[right]=cur[right],cur[left]
                    left +=1
                    right -=1
            result.append(cur)
            queue=nextNode
        return result