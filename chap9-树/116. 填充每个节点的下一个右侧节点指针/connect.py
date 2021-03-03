"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        queue = [root]
        while len(queue) > 0:
            curLength = len(queue)
            nextNode = []
            for index in range(curLength):
                if queue[index].left != None:
                    nextNode.append(queue[index].left)
                if queue[index].right != None:
                    nextNode.append(queue[index].right)
                if index < curLength - 1:
                    queue[index].next = queue[index + 1]

            if len(nextNode) > 0:
                queue = nextNode
            else:
                break
        return root
