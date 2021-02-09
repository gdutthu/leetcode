class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxVal = float("-inf")
        secondVal = float("-inf")
        thirdVal = float("-inf")

        count = 0  # 统计数值转移次数

        for index in range(len(nums)):

            if nums[index] > maxVal:
                thirdVal = secondVal
                secondVal = maxVal
                maxVal = nums[index]
                count += 1
            elif nums[index] > secondVal and nums[index] < maxVal:
                thirdVal = secondVal
                secondVal = nums[index]
                count += 1

            elif nums[index] > thirdVal and nums[index] < secondVal:
                thirdVal = nums[index]
                count += 1
            print(maxVal, secondVal, thirdVal)
        if count >= 3:
            return thirdVal
        else:
            return maxVal