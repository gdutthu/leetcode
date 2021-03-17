class Solution:
    def numDecodings(self, s: str) -> int:
        string = list(s)  # 将字符串转化为字符列表
        length = len(string)  # 字符列表的长度

        # 将str类型数据转化为int类型
        for index in range(length):
            string[index] = int(string[index])

        # 第一个字符若以0开头，整个字符串都无法进行解码
        if string[0] == 0:
            return 0
        # 只有一个字符时候
        elif length == 1:
            return 1

        # count[i]:代表第0~i个字符串的编码方法
        count = [0] * (length + 1)
        count[0] = 1  # 字符串为空时有一种解码方法

        for index in range(1, length + 1):
            if string[index - 1] != 0:
                count[index] = count[index - 1]
            if 1 <= string[index - 2] and string[index - 2] <= 2:
                item = string[index - 2] * 10 + string[index - 1]
                if 1 <= item and item <= 26:
                    count[index] += count[index - 2]
        return count[-1]