class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row=len(triangle)       # 三角形有多少行
        col=row                 # 三角形最后一行的元素个数

        # count[i][j]:代表三角形自顶向下到达第i行，第j列的最小路径和
        count=[[0 for i in range(col)] for j in range(row)]

        for rowIndex in range(row):
            # 三角形的第rowIndex行(从0开始计算)最多有rowIndex+1个元素(从1开始计算)
            num=rowIndex+1

            for colIndex in range(num):

                if colIndex==0:           # 第一列坐标
                    if rowIndex==0:
                        count[0][0]=triangle[0][0]     # 顶点坐标
                    else:
                        count[rowIndex][0]=triangle[rowIndex][0]+count[rowIndex-1][0]
                elif colIndex==num-1:     # 最后一列坐标
                    count[rowIndex][colIndex]=triangle[rowIndex][colIndex]+count[rowIndex-1][colIndex-1]
                elif 0<colIndex<num-1:    # 其余坐标
                    item=min(count[rowIndex-1][colIndex],count[rowIndex-1][colIndex-1])
                    count[rowIndex][colIndex]=triangle[rowIndex][colIndex]+item
        minPathSum=min(count[-1])
        return minPathSum