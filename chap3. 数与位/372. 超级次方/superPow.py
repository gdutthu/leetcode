class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # step1:先计算b数组代表的整数
        n = 0
        length = len(b)
        for index in range(length):
            n += b[index] * (10 ** (length - 1 - index))

        # step2:计算a^n
        if n == 0:
            return 1
        elif n > 0:
            res = self.pow(a, n)
            return res
        elif n < 0:
            res = self.pow(a, -n)
            return 1 / res

    # 函数功能：num为非负数，n为非负数,计算num^n
    def pow(self, num, n):
        if n == 0:
            return 1
        elif n == 1:
            return num

        if n % 2 == 0:
            item = self.pow(num, n // 2)
            return (item * item) % 1337
        else:
            item = self.pow(num, (n - 1) // 2)
            return (item * item * num) % 1337