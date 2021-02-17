"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        arr=[]
        for node in root.children:
            res=self.postorder(node)
            if len(res)>0:
                for i in res:
                    arr.append(i)
        arr.append(root.val)
        return arr