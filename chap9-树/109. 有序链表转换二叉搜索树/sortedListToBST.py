# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        root = self.buildTree(arr)
        return root

    def buildTree(self, arr):
        if len(arr) == 0:
            return None
        left = 0
        right = len(arr) - 1
        headIndex = (left + right) // 2
        head = TreeNode(arr[headIndex])
        head.left = self.buildTree(arr[:headIndex])
        head.right = self.buildTree(arr[(headIndex + 1):])
        return head