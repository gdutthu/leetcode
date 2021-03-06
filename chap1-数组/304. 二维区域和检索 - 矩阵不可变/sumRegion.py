class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr=matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        count=0
        for rowIndex in range(row1,row2+1):
            for colIndex in range(col1,col2+1):
                count +=self.arr[rowIndex][colIndex]
        return count

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)