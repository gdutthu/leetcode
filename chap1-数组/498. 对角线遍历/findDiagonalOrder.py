class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]:
            return []
        row=len(matrix)
        col=len(matrix[0])
        arr=[]
        # 待打印线段的左右端点坐标
        leftRow,leftCol=0,0
        rightRow,rightCol=0,0
        #toPrint=False时，左向右打印，toPrint=True时，右向左打印
        toPrint=False
        while leftCol<col:
            if toPrint==False:  # 左向右打印
                for i in range(leftRow-rightRow+1):
                    item=matrix[leftRow-i][leftCol+i]
                    arr.append(item)
            elif toPrint==True: # 右向左打印
                for i in range(leftRow-rightRow+1):
                    item=matrix[rightRow+i][rightCol-i]
                    arr.append(item)
            toPrint=bool(1-toPrint)
            # 更新待打印线段的端点坐标
            if leftRow<row-1:
                leftRow +=1
            else:
                leftCol +=1
            if rightCol<col-1:
                rightCol +=1
            else:
                rightRow +=1
        return arr