class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            res = self.pow(x, n)
            return res
        elif n < 0:
            res = self.pow(x, -n)
            return 1 / res

    # 函数功能：num为非负数，n为非负数,计算num^n
    def pow(self, num, n):
        if n == 0:
            return 1
        elif n == 1:
            return num

        if n % 2 == 0:
            item = self.pow(num, n // 2)
            return item * item
        else:
            item = self.pow(num, (n - 1) // 2)
            return item * item * num