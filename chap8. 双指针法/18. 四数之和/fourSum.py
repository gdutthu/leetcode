class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        if length < 4:
            return []

        data = {}  # 哈希表，防止答案重复
        res = []  # 返回结果
        nums = sorted(nums)

        for index in range(length - 3):
            first = nums[index]

            for i in range(index + 1, length - 2):
                second = nums[i]
                left = i + 1
                right = length - 1
                while left < right:
                    item = first + second + nums[left] + nums[right]
                    if item < target:
                        left += 1
                    elif item > target:
                        right -= 1
                    elif item == target:
                        cur = [first, second, nums[left], nums[right]]
                        cur = sorted(cur)
                        if (first, second, nums[left], nums[right]) not in data:
                            data[first, second, nums[left], nums[right]] = 1
                            res.append(cur)
                        left += 1
        return res