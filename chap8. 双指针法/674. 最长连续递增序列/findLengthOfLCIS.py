class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length=len(nums)
        if length==0 or length==1:
            return length


        maxLength=1  # 初始化递增子序列的最大长度
        left=0       # 初始化递增子序列的左、右边界下标
        right=0
        while right+1<length:
            if nums[right]<nums[right+1]:
                right +=1
                maxLength=max(maxLength,right-left+1)
            elif nums[right]>=nums[right+1]:
                maxLength=max(maxLength,right-left+1)
                left =right+1
                right=right+1
        return maxLength