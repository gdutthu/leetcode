# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def __init__(self):
        self.arr=[]
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root==None:
            return []
        cur=[]
        self.node_sum(root,cur,targetSum)
        return self.arr

    def node_sum(self,root,cur,targetSum):
        if root==None:
            return
        cur.append(root.val)
        if root.left==None and root.right==None:
            if  sum(cur)==targetSum:
                self.arr.append(copy.copy(cur))
        self.node_sum(root.left,cur,targetSum)
        self.node_sum(root.right,cur,targetSum)
        cur.pop()
        return