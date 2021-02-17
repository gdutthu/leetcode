# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        arr=[]

        leftArr=self.postorderTraversal(root.left)
        if len(leftArr)>0:
            for node in leftArr:
                arr.append(node)
        rightArr=self.postorderTraversal(root.right)
        if len(rightArr)>0:
            for node in rightArr:
                arr.append(node)
        arr.append(root.val)
        return arr