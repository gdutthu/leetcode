class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)  # 二维数组的行、列
        cols = len(obstacleGrid[0])

        # 初始化二维数组，记录能走到网格不同位置的的方法
        pathCount = [[0 for i in range(cols)] for j in range(rows)]
        pathCount[0][0] = 1  # 起始点为原点，只有一种方法到达

        for row in range(rows):
            for col in range(cols):
                # 起始点位置数值已经初始化好了，不再进行任何修改

                if obstacleGrid[row][col] == 1:  # 该位置为障碍物的话，则无法到该位置
                    pathCount[row][col] = 0
                    continue

                if row == 0 and col > 0:  # 第一行元素,只能向右走
                    pathCount[row][col] = pathCount[row][col - 1]

                elif col == 0 and row > 0:  # 第一列元素,只能向下走
                    pathCount[row][col] = pathCount[row - 1][col]
                elif row > 0 and col > 0:  # 其他位置元素,可以向下或者向右走
                    pathCount[row][col] = pathCount[row - 1][col] + pathCount[row][col - 1]
        return pathCount[rows - 1][cols - 1]
