class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 情况1：只有三个数，没得选
        if len(nums)==3:
            return nums[-1]*nums[-2]*nums[-3]

        nums=sorted(nums)

        # 情况2：全正数，返回最大的三个数相乘
        if nums[0]>=0 and nums[-1]>=0:
            return nums[-1]*nums[-2]*nums[-3]
        # 情况3：全负数，返回最大的三个数相乘

        elif nums[0]<=0 and nums[-1]<=0:
            return nums[-1]*nums[-2]*nums[-3]
        # 情况4：有正有负，最大值：两个负数*最大的正数，或者，最大的三个数相乘
        else:
            return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])