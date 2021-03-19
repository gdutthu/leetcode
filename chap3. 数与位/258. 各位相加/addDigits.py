class Solution:
    def addDigits(self, num: int) -> int:
        remaing = self.calculate(num)

        while remaing > 9:
            remaing = self.calculate(remaing)
        return remaing

    # 函数功能：计算一个数的各个位数的和
    def calculate(self, num):
        count = 0
        while num > 0:
            s = num // 10
            y = num % 10  # 余数
            count += y
            if s == 0:
                break
            num = s
        return count