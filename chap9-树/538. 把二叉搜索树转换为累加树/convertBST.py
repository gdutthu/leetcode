# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root

        # 二叉树的中序遍历数组，也是升序数组
        nodeArr = self.inorder(root)
        # 存放二叉树各节点信息
        nodeIndex = {}
        for index in range(len(nodeArr)):
            if nodeArr[index] not in nodeIndex:
                nodeIndex[nodeArr[index]] = index
        self.Bst(root, nodeArr, nodeIndex)
        return root

    def Bst(self, root, nodeArr, nodeIndex):
        if root == None:
            return
        index = nodeIndex[root.val]
        newVal = sum(nodeArr[index:])
        root.val = newVal
        self.Bst(root.left, nodeArr, nodeIndex)
        self.Bst(root.right, nodeArr, nodeIndex)

    # 函数功能：二叉树的中序遍历
    # 注意二叉搜索树的中序遍历是升序数组
    def inorder(self, root):
        if root == None:
            return []
        arr = []
        leftArr = self.inorder(root.left)
        if len(leftArr) > 0:
            for node in leftArr:
                arr.append(node)
        arr.append(root.val)
        rightArr = self.inorder(root.right)
        if len(rightArr) > 0:
            for node in rightArr:
                arr.append(node)
        return arr