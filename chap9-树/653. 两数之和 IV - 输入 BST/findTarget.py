# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root == None:
            return False
        arr = self.inorder_print(root)
        left = 0
        right = len(arr) - 1
        while left < right:
            item = arr[left] + arr[right]
            if item == k:
                return True
            elif item < k:
                left += 1
            elif item > k:
                right -= 1
        return False

    # 函数功能：二叉树的中序遍历，搜索二叉树的中序遍历是升序数列
    def inorder_print(self, root):
        if root == None:
            return []
        arr = []
        leftArr = self.inorder_print(root.left)
        if len(leftArr) > 0:
            for node in leftArr:
                arr.append(node)
        arr.append(root.val)
        rightArr = self.inorder_print(root.right)
        if len(rightArr) > 0:
            for node in rightArr:
                arr.append(node)
        return arr