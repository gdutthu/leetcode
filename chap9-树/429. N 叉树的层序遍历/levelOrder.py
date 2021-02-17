"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None:
            return []
        queue=[root]
        arr=[]
        while len(queue)>0:
            cur=[]
            nextNode=[]
            for node in queue:
                if node!=None:
                    cur.append(node.val)
                    for i in node.children:
                        nextNode.append(i)
            if len(cur)>0:
                arr.append(cur)
                queue=nextNode
            else:
                break
        return arr