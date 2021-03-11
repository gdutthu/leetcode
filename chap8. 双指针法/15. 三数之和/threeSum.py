class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []

        res = []  # 储存满足要求的三数之和
        data = {}  # 哈希表，防止结果重复
        nums = sorted(nums)
        for index in range(length - 2):
            first = nums[index]
            left = index + 1
            right = length - 1
            while left < right:
                item = first + nums[left] + nums[right]
                if item < 0:
                    left += 1
                elif item == 0:
                    cur = [first, nums[left], nums[right]]
                    if (first, nums[left], nums[right]) not in data:
                        data[first, nums[left], nums[right]] = 1
                        res.append(cur)
                    left += 1
                elif item > 0:
                    right -= 1
        return res