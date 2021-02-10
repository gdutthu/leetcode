import copy
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        arr=copy.copy(nums)
        for index in range(length):
            new_index=(index+k)%length
            arr[new_index]=nums[index]

        for index in range(length):
            nums[index]=arr[index]
