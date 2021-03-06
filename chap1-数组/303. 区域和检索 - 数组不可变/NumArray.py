class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=nums


    def sumRange(self, i: int, j: int) -> int:
        count=0
        for index in range(i,j+1):
            count +=self.arr[index]
        return count


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)