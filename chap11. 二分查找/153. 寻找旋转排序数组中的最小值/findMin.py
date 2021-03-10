class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 基本思路:旋转数组=升序的大数值数组+升序的小数值数组，最小值为升序的小数值数组的第一位数
        # 最小值的搜索也变成搜索右有序数组的第一位数字
        left=0
        right=len(nums)-1
        while left<=right:
            if left==right:
                return nums[left]
            mid=(left+right)//2
            # 情况1:右侧数组为有序数组，则进一步缩小搜索区间
            if nums[mid]<nums[right]:
                right=mid
            # 情况2：右侧数组不为有序数组，该段区间必定同时含有(升序的大数值数组+升序的小数值数组)
            # 则去掉左侧的大数值升序数组
            elif nums[mid]>nums[right]:
                left=mid+1
