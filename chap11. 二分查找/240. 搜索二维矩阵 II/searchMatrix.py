class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        rows = len(matrix)  # 二维数组的行、列
        cols = len(matrix[0])
        rowIndex = 0        # 搜索起点设置为右上角
        colIndex = cols - 1
        while rowIndex < rows and colIndex >= 0:
            if matrix[rowIndex][colIndex] == target:
                return True
            elif matrix[rowIndex][colIndex] < target:
                rowIndex += 1
            elif matrix[rowIndex][colIndex] > target:
                colIndex -= 1
        return False