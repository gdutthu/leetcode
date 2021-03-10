class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index1 = 0  # 不重复元素的移动下标

        index = 1
        while index < len(nums):
            if nums[index] != nums[index1]:
                index1 += 1
                nums[index1] = nums[index]
            index += 1
        return index1 + 1