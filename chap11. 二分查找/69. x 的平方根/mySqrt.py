class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left = 1
        right = x
        while left < right:
            mid = (left + right) // 2
            res = mid ** 2
            if res == x:
                return mid
            elif res > x:
                right = mid - 1
            elif res < x:
                # 平方根是小数时，进行向下取整
                if right - left == 1:
                    right_power = right ** 2
                    if right_power <= x:
                        return right
                    else:
                        return left

                else:
                    left = mid
        return left