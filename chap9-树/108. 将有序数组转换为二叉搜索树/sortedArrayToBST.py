# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1
        headIndex = (left + right) // 2
        head = TreeNode(nums[headIndex])
        head.left = self.sortedArrayToBST(nums[:headIndex])
        head.right = self.sortedArrayToBST(nums[(headIndex + 1):])
        return head