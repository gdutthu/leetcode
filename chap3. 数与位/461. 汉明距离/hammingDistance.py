class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # step1：将十进制数字转为二进制
        arr1 = self.transfer(x)
        arr2 = self.transfer(y)
        length1 = len(arr1)
        length2 = len(arr2)
        # 将二进制的位数调整到一致
        if length1 < length2:
            for i in range(length2 - length1):
                arr1.append(0)
        elif length1 > length2:
            for i in range(length1 - length2):
                arr2.append(0)
        # step2：计算汉明距离
        count = 0
        for index in range(max(length1, length2)):
            if arr1[index] != arr2[index]:
                count += 1
        return count

    # 函数功能：将十进制数转为二进制
    def transfer(self, num):
        arr = []
        while num >= 0:
            s = num // 2
            y = num % 2
            arr.append(y)
            if s == 0:
                break
            num = s
        return arr