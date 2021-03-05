# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        arr=self.inorder(root)
        length=len(arr)
        count=[1]*length
        maxTimes=0
        for index in range(length):
            if index>0 and arr[index]==arr[index-1]:
                count[index] =count[index-1]+1
            maxTimes=max(maxTimes,count[index])
        res=[]
        for index in range(length):
            if count[index]==maxTimes :
                res.append(arr[index])
        return res

    # 函数功能：二叉树的中序遍历，二叉搜索树的中序遍历是升序数组
    def inorder(self,root):
        if root==None:
            return []
        arr=[]
        left=self.inorder(root.left)
        if len(left)>0:
            for node in left:
                arr.append(node)
        arr.append(root.val)
        right=self.inorder(root.right)
        if len(right):
            for node in right:
                arr.append(node)
        return arr