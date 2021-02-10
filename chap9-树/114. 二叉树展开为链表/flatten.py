# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = self.prePrint(root)
        length = len(arr)
        if length >= 2:
            for index in range(length):
                arr[index].left = None
                if index < length - 1:
                    arr[index].right = arr[index + 1]
                else:
                    arr[index].right = None

    # 函数功能：函数的先序遍历
    def prePrint(self, root):
        if root == None:
            return []
        arr = []
        arr.append(root)

        leftArr = self.prePrint(root.left)
        if len(leftArr) > 0:
            for node in leftArr:
                arr.append(node)
        rightArr = self.prePrint(root.right)
        if len(rightArr) > 0:
            for node in rightArr:
                arr.append(node)
        return arr