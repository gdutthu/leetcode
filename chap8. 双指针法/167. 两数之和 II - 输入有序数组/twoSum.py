class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            item=numbers[left]+numbers[right]
            if item<target:
                left +=1
            elif item>target:
                right -=1
            elif item==target:
                return [left+1,right+1]