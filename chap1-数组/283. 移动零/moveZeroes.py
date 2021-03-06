class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)

        notZeroIndex=0
        index=0
        while index<length:
            if nums[index]!=0:
                nums[notZeroIndex],nums[index]=nums[index],nums[notZeroIndex]
                notZeroIndex +=1
            index+=1
        for i in range(index,length):
            nums[i]=0
