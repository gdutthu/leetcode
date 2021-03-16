class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count=[[1 for i in range(n)] for j in range(m)]
        for row in range(0,m):
            for col in range(0,n):
                #对原点位置初始化为1
                if row==0 and col>0:    #第一行
                    count[row][col]=count[row][col-1]
                elif row>0 and col==0: #第一列
                    count[row][col]=count[row][col-1]

                elif row>0 and col>0:
                    count[row][col]=count[row-1][col]+count[row][col-1]
        return count[m-1][n-1]
