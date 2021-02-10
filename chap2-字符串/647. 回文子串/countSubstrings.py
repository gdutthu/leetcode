class Solution:
    def countSubstrings(self, s: str) -> int:
        string = list(s)  # 将字符串转化为列表
        length = len(string)
        num = 0  # 统计回文字符串个数
        for index in range(length):

            # 情况1：回文字符串字符个数为奇数
            count = 0
            while index - count >= 0 and index + count <= length - 1 and string[index - count] == string[index + count]:
                num += 1
                count += 1

            # 情况2：回文字符串字符个数为偶数
            count = 0
            left = index
            right = index + 1
            while left - count >= 0 and right + count <= length - 1 and string[left - count] == string[right + count]:
                num += 1
                count += 1

        return num