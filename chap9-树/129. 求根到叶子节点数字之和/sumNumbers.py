# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.path = []
        self.nodePtah(root, [])
        count = 0
        for arr in self.path:
            index = 0
            item = 0
            while index < len(arr):
                item += arr[-(index + 1)] * (10 ** index)
                index += 1
            count += item
        return count

    # 函数功能：记录根到叶子节点的所有路径
    def nodePtah(self, root, cur):
        if root == None:
            return
        cur.append(root.val)
        if root.left == None and root.right == None:
            self.path.append(copy.copy(cur))
        self.nodePtah(root.left, cur)
        self.nodePtah(root.right, cur)
        cur.pop()