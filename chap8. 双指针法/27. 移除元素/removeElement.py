class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_val_index=0
        length=0
        for i in range(len(nums)):
            if nums[i]!=val:
                length +=1
                nums[not_val_index]=nums[i]
                not_val_index +=1
        return length