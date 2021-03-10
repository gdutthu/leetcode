class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 对于每个房屋，要么用前面的暖气，要么用后面的，二者取近的，得到距离；
        # 对于所有的房屋，选择最大的上述距离。

        heaters = sorted(heaters)
        heaters_nums = len(heaters)  # 供暖片的数量

        radius = float("-inf")  # 供暖片的最小供暖半径,即count数组的最大值

        for index in range(len(houses)):
            # 计算当前房屋到每个暖气片的距离
            # 采用二分法进行搜索左右两侧离当前房屋最近的供暖片
            left = 0
            right = heaters_nums - 1
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] < houses[index]:
                    left = mid + 1
                else:
                    right = mid - 1

            # 再计算左右两侧最近供暖片与当前房屋的距离
            if left >= heaters_nums:
                left_distance = float("inf")
            else:
                left_distance = abs(houses[index] - heaters[left])

            if right < 0:
                right_distance = float("inf")
            else:
                right_distance = abs(houses[index] - heaters[right])

            # 更新供暖片的最小半径
            radius = max(radius, min(left_distance, right_distance))
        return radius