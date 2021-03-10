class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index1 = 0  # 不重复元素的下标

        index = 1  # 数组移动下标
        while index < len(nums):
            if nums[index] != nums[index1]:
                index1 += 1
                nums[index1] = nums[index]
            elif nums[index1] == nums[index]:
                # 不存在重复元素
                if (index1 - 1 >= 0 and nums[index1 - 1] != nums[index]) or index1 == 0:
                    index1 += 1
                    nums[index1] = nums[index]
            index += 1
        return index1 + 1
