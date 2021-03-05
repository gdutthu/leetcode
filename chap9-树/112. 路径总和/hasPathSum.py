# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        self.path = []
        self.tree_path(root, [], targetSum)
        if len(self.path) > 0:
            return True
        else:
            return False

    def tree_path(self, root, cur, targetSum):
        if root == None:
            return
        cur.append(root.val)
        if root.left == None and root.right == None:
            if sum(cur) == targetSum:
                self.path.append(copy.copy(cur))
        if root.left != None:
            self.tree_path(root.left, cur, targetSum)
        if root.right != None:
            self.tree_path(root.right, cur, targetSum)
        cur.pop()
        return