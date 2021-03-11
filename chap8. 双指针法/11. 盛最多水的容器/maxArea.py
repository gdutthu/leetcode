class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0  # 初始化容器体积
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                area = max(area, height[left] * (right - left))
                left = left + 1
            else:
                area = max(area, height[right] * (right - left))
                right = right - 1

        return area