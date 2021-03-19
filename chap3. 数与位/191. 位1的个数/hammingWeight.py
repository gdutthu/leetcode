class Solution:
    def hammingWeight(self, n: int) -> int:
        # 将十进制转化为二进制
        times = 0
        while True:
            s = n // 2  # 商
            item = n % 2  # 余数
            if item == 1:
                times += 1

            if s == 0:
                break
            n = s
        return times