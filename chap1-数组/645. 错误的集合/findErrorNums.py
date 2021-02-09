class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        array = [None] * length
        first = None
        second = None
        # 数组的下标是从0开始，问题提供的数字是从1开始
        for index in range(length):
            i = nums[index]
            if array[i - 1] == None:
                array[i - 1] = i
            else:
                first = i

        for index in range(length):
            if array[index] == None:
                second = index + 1
                break
        return [first, second]