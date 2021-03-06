class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 通俗的理解，n-1个少数民族加分相当于1个民族扣分
        minVal=min(nums)
        count=0
        for index in range(len(nums)):
            count+=(nums[index]-minVal)
        return count