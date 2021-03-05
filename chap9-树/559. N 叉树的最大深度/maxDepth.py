"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        queue=[root]
        depth=0
        while len(queue)>0:
            depth +=1
            nextNode=[]
            for node in queue:
                for children in node.children:
                    if children !=None:
                        nextNode.append(children)
            if len(nextNode)>0:
                queue=nextNode
            else:
                break
        return depth