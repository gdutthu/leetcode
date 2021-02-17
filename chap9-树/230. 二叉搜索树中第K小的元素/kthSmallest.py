# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array = self.inorderPrint(root)
        return array[k - 1]

    # 函数功能：二叉树的中序遍历
    # 特别注意：二叉搜索树的中序遍历是升序数组
    def inorderPrint(self, root):
        array = []

        if root == None:
            return []

        leftArray = self.inorderPrint(root.left)
        if len(leftArray) > 0:
            for node in leftArray:
                array.append(node)

        array.append(root.val)

        rightArray = self.inorderPrint(root.right)
        if len(rightArray) > 0:
            for node in rightArray:
                array.append(node)

        return array