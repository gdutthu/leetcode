class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 将所有正数作为数组下标，置对应数组值为负值。
        # 那么，仍为正数的位置即为（未出现过）消失的数字。
        for item in nums:
            index = abs(item) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        res = []
        for index in range(len(nums)):
            if nums[index] > 0:
                res.append(index + 1)
        return res