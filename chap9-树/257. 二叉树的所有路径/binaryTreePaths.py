# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        self.path = []
        self.nodePtah(root, [])
        pathStr = self.list_to_string(self.path, [])
        return pathStr

    # 函数功能：用列表形式存放所有路径
    def nodePtah(self, root, cur):
        if root == None:
            return
        cur.append(root.val)
        if root.left == None and root.right == None:
            self.path.append(copy.copy(cur))
        self.nodePtah(root.left, cur)
        self.nodePtah(root.right, cur)
        cur.pop()

    # 函数功能：将列表形式的路径转化为字符串形式
    def list_to_string(self, pathArr, pathStr):
        if len(pathArr) == 0:
            return
        for path in pathArr:
            string = ""
            length = len(path)
            for index in range(length):
                item = str(path[index])
                if index < length - 1:
                    string += item + "->"
                else:
                    string += item
            pathStr.append(string)
        return pathStr
