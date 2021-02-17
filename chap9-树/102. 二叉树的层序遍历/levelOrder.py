# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        queue=[root]
        arr=[]
        while len(queue)>0:
            nextNode=[]
            cur=[]
            for node in queue:
                if node!=None:
                    cur.append(node.val)
                    nextNode.append(node.left)
                    nextNode.append(node.right)
            if len(cur)>0:
                arr.append(cur)
                queue=nextNode
            else:
                break
        return arr
