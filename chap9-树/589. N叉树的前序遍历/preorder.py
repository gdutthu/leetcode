"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = self.prePrint(root)
        return arr

    def prePrint(self, root):
        if root == None:
            return []
        arr = []
        arr.append(root.val)

        for node in root.children:
            cur = self.prePrint(node)
            if len(cur) > 0:
                for item in cur:
                    arr.append(item)
        return arr