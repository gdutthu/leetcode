# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        # 二叉树的中序遍历
        # 注意，二叉搜索树的中序遍历是升序数组
        self.array = self.inorderPrint(root)

        self.arrayLength = len(self.array)  # 二叉树元素个数

        # 记录已经遍历到二叉树的数值的下标
        self.numIndex = -1

    # 函数功能：实现二叉树的中序遍历
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

    def next(self) -> int:
        """
        @return the next smallest number
        """
        item = self.array[self.numIndex + 1]
        self.numIndex += 1
        return item

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.numIndex < self.arrayLength - 1:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()