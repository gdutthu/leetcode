# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        arr = self.prePrint(root)
        return arr

    def prePrint(self, root):
        if root == None:
            return []
        arr = []
        arr.append(root.val)

        leftArr = self.prePrint(root.left)
        if len(leftArr) > 0:
            for node in leftArr:
                arr.append(node)

        rightArr = self.prePrint(root.right)
        if len(rightArr) > 0:
            for node in rightArr:
                arr.append(node)
        return arr