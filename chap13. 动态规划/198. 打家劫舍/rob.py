class Solution:
    def rob(self, nums: List[int]) -> int:
        houseNum = len(nums)  # 房屋数量
        if houseNum == 0:
            return 0
        elif houseNum == 1:
            return nums[0]

        # 基本思路：
        # 1、第一个房子只能直接偷窃
        # 2、其他房子，分为偷窃和不偷窃两种情况

        # count[i]:代表从第1个房子~第i个房子，盗匪能获取的最大利润
        count = [0] * (houseNum + 1)
        count[1] = nums[0]

        for index in range(2, houseNum + 1):
            count[index] = max(count[index - 1], count[index - 2] + nums[index - 1])
        return count[-1]