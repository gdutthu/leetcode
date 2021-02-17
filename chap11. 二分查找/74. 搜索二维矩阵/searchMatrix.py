class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix==[] or matrix==[[]]:
            return False

        rows=len(matrix)     #数组的行、列
        cols=len(matrix[0])


        #从二维数组的右上端点开始搜索
        rowIndex=0
        colIndex=cols-1

        while rowIndex<rows and colIndex>=0:
            if matrix[rowIndex][colIndex]==target:
                return True
            elif matrix[rowIndex][colIndex]<target:
                rowIndex +=1
            elif matrix[rowIndex][colIndex]>target:
                colIndex -=1
        return False