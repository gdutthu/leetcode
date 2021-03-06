class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)      #二维矩阵的行、列
        col=len(matrix[0])


        leftRow,leftCol=0,0 # 打印区域的左上、右下端点坐标
        rightRow,rightCol=row-1,col-1

        arr=[]              # 储存元素
        while leftRow<=rightRow and leftCol<=rightCol:
            # 特殊情形，只剩下一行或一列元素
            if leftRow==rightRow:
                for index in range(leftCol,rightCol+1):
                    arr.append(matrix[leftRow][index])
                break
            elif leftCol==rightCol:
                for index in range(leftRow,rightRow+1):
                    arr.append(matrix[index][leftCol])
                break
            # 其余时刻，按照顺时针方向打印外围四行元素
            for index in range(leftCol,rightCol):
                arr.append(matrix[leftRow][index])
            for index in range(leftRow,rightRow):
                arr.append(matrix[index][rightCol])
            for index in range(rightCol,leftCol,-1):
                arr.append(matrix[rightRow][index])
            for index in range(rightRow,leftRow,-1):
                arr.append(matrix[index][leftCol])

            # 更新端点坐标
            leftRow +=1
            leftCol +=1
            rightCol-=1
            rightRow-=1
        return arr