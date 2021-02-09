class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length=len(nums)
        maxLength=0
        cur=0

        for index in range(length):
            if nums[index]==1:
                cur +=1
            else:
                cur=0
            maxLength=max(maxLength,cur)
        return maxLength