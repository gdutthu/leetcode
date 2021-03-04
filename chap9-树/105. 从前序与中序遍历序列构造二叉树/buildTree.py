# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        headVal=preorder.pop(0)
        head=TreeNode(headVal)

        index=0
        while index<len(inorder):
            if inorder[index]==headVal:
                break
            else:
                index +=1
        head.left=self.buildTree(preorder[:index],inorder[:index])
        head.right=self.buildTree(preorder[index:],inorder[index+1:])

        return head