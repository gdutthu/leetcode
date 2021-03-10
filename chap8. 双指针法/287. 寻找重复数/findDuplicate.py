class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lenth=len(nums)
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]<0:
                return index+1
            nums[index]=-nums[index]