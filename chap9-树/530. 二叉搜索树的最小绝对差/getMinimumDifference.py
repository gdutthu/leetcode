# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 二叉搜索树的中序遍历
        # 二叉搜索树的中序遍历是升序遍历
        array = self.inorderPrint(root)

        minGap = array[1] - array[0]
        for index in range(len(array) - 1):
            minGap = min(minGap, array[index + 1] - array[index])
        return minGap

    # 函数功能：二叉树的中序遍历
    def inorderPrint(self, root):
        if root == None:
            return []
        array = []
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