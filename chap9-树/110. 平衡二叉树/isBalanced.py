# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        left=self.nodeHeight(root.left)
        right=self.nodeHeight(root.right)
        if abs(left-right)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    # 函数功能：二叉树中节点的高度
    def nodeHeight(self,root):
        if root==None:
            return 0
        left=self.nodeHeight(root.left)
        right=self.nodeHeight(root.right)
        return max(left,right)+1