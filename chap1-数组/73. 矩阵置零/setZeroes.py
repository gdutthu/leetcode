from copy import deepcopy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)     # 二维矩阵的行、列
        col=len(matrix[0])

        arr=deepcopy(matrix)

        for rowIndex in range(row):
            for colIndex in range(col):
                # 检测到0元素，把当前行、列元素全部置0
                if arr[rowIndex][colIndex]==0:
                    for i in range(col):
                        matrix[rowIndex][i]=0
                    for j in range(row):
                        matrix[j][colIndex]=0