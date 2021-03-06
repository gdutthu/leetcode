# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        isEqual = self.isEqual(s, t)
        if isEqual == True:
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

            # 函数功能：判断两个节点所生成的二叉树是否等价

    def isEqual(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None and root2 != None:
            return False
        elif root1 != None and root2 == None:
            return False

        if root1.val != root2.val:
            return False
        return self.isEqual(root1.left, root2.left) and self.isEqual(root1.right, root2.right)