# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        count = 0  # 记录二叉树所有左子树的和

        queue = []  # 层序遍历的辅助队列结构
        queue.append(root)
        nodeInfo = ["head"]  # 记录当前层每一个节点属于父母节点的哪一个儿子节点

        while len(queue) > 0:
            nextLevelNode = []  # 记录下一层节点
            nextLevelNodeInfo = []  # 记录下一层节点是属于父母节点的哪一个儿子节点

            for index in range(len(queue)):  # 遍历当前层节点
                node = queue[index]
                if node != None:
                    # 当前节点为叶子节点
                    if node.left == None and node.right == None:
                        if nodeInfo[index] == "left":  # 当前叶子节点为左叶子节点
                            count += node.val
                    else:
                        nextLevelNode.append(node.left)
                        nextLevelNodeInfo.append("left")
                        nextLevelNode.append(node.right)
                        nextLevelNodeInfo.append("right")
            queue = nextLevelNode
            nodeInfo = nextLevelNodeInfo
        return count