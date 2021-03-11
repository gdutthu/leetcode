class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minGap=float("inf")   # 三数之和与target的差距
        res=None              # 三数之和
        nums=sorted(nums)
        length=len(nums)


        for index in range(length-2):
            first=nums[index]
            left=index+1
            right=length-1
            while left<right:
                item=first+nums[left]+nums[right]
                if abs(item-target)<minGap:
                    minGap=abs(item-target)
                    res=item
                if item<=target:
                    left +=1
                else:
                    right -=1
        return res