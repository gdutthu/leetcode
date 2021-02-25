class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)  # 原矩阵的行、列数
        col = len(nums[0])
        # 情况1：无法进行矩阵转化，则输出原矩阵
        if r * c != row * col:
            return nums
        # 情况2：可以进行矩阵转化
        # 原二维矩阵的数值元素
        val = []
        for i in range(row):
            for j in range(col):
                val.append(nums[i][j])
        res = [[0 for i in range(c)] for j in range(r)]

        for row in range(r):
            for col in range(c):
                res[row][col] = val[row * c + col]
        return res