class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        # 初始化螺旋矩阵
        arr = [[1 for i in range(n)] for j in range(n)]
        # 初始化左上、右下端点的坐标
        leftRow, leftCol = 0, 0
        rightRow, rightCol = n - 1, n - 1
        item = 1
        while item <= n ** 2 and leftRow <= rightRow:
            # 特殊情形，只剩下一行元素
            if leftRow == rightRow:
                for index in range(leftCol, rightRow + 1, 1):
                    arr[leftRow][index] = item
                    item += 1
                break

            # 其余时刻，给外围四行元素进行进行重新复制
            for index in range(leftCol, rightCol):
                arr[leftRow][index] = item
                item += 1
            for index in range(leftRow, rightRow):
                arr[index][rightCol] = item
                item += 1
            for index in range(rightCol, leftCol, -1):
                arr[rightRow][index] = item
                item += 1
            for index in range(rightRow, leftRow, -1):
                arr[index][leftCol] = item
                item += 1

            # 更新端点坐标
            leftCol += 1
            leftRow += 1
            rightRow -= 1
            rightCol -= 1
        return arr
