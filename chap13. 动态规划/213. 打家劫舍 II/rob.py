class Solution:
    def rob(self, nums: List[int]) -> int:
        houseNum = len(nums)  # 房屋数量

        if houseNum == 0:
            return 0
        elif houseNum == 1:
            return nums[0]

        # 基本思路：
        # 1、第一个房子要是被偷窃，最后一个房子就不能被偷窃。同理，最后一个房子要是被偷窃，第一个房子就不能被偷窃
        # 2、其他房子，分为偷窃和不偷窃两种情况

        # firstcount[i]:代表在偷窃第一个房子的前提下，从第1个房子~第i个房子，盗匪能获取的最大利润
        # 此时最后一个房子一定不能被偷窃
        firstcount = [0] * (houseNum + 1)
        firstcount[1] = nums[0]
        for index in range(2, houseNum):
            firstcount[index] = max(firstcount[index - 1], firstcount[index - 2] + nums[index - 1])

        # notFirstcount[i]:代表在不偷窃第一个房子的前提下，从第1个房子~第i个房子，盗匪能获取的最大利润
        # 此时最后一个房子被偷窃,第一个房子不能被偷窃。其实就是按照上面的计算方法,逆序进行计算即可
        notFirstcount = [0] * (houseNum + 1)
        notFirstcount[houseNum - 1] = nums[houseNum - 1]
        for index in range(houseNum - 2, 0, -1):
            notFirstcount[index] = max(notFirstcount[index + 1], notFirstcount[index + 2] + nums[index])

        return max(notFirstcount[1], firstcount[-2])
