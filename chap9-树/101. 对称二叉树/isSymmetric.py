# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        queue = []        # 层序遍历的队列结构
        queue.append(root)
        while len(queue) > 0:
            cur = []       # 下一层二叉树节点
            isLeaf = True  # 判断是否是最后一层二叉树
            for node in queue:
                if node != None:
                    cur.append(node.left)
                    cur.append(node.right)
                    isLeaf = False
                else:
                    cur.append(None)
                    cur.append(None)

            if isLeaf == False:
                length = len(cur)
                for index in range(length // 2):
                    if cur[index] == None or cur[length - 1 - index] == None:
                        if cur[index] != None or cur[length - 1 - index] != None:
                            return False
                    elif cur[index].val != cur[length - 1 - index].val:
                        return False
                queue = cur
            else:
                break
        return True