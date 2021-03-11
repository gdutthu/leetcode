class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=len(nums)        # 数组元素个数
        minLength=float("inf")  # 满足要求的连续子数组的最小长度

        left=0          # 初始化滑动窗口的左右边界下标
        right=0
        count=nums[0]   # 初始化滑动窗口元素之和

        while right<length and left<=right:
            if count<target:   # 滑动窗口元素之和<target，右指针右移
                if right+1<length:
                    right +=1
                    count +=nums[right]
                else:
                    break
            else:             # 滑动窗口元素之和>=target，满足要求
                minLength=min(minLength,right-left+1)
                if left+1<length:
                    count -=nums[left]
                    left +=1
                else:
                    break

        if minLength==float("inf"):
            return 0
        else:
            return minLength