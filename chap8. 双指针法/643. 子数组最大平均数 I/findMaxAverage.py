class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        maxAverage = float("-inf")

        left = 0  # 滑动窗口的左、右下标
        right = 0
        count = nums[0]  # 滑动窗口的元素之和
        while right < length:
            if right - left + 1 < k:
                if right + 1 < length:
                    right += 1
                    count += nums[right]
                else:
                    break
            elif right - left + 1 == k:
                maxAverage = max(maxAverage, count / k)
                count -= nums[left]
                left += 1
        return maxAverage