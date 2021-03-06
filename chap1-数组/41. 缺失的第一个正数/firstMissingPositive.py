class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        data = {}
        for index in range(len(nums)):
            if nums[index] > 0 and (nums[index] not in data):
                data[nums[index]] = 1

        item = 1
        while True:
            if item in data:
                item += 1
            else:
                return item