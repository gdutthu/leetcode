class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 0:
            return []
        result = [[1]]
        for index in range(1, numRows):
            cur = [1] * (index + 1)
            pre = result[index - 1]
            for i in range(1, index):
                cur[i] = pre[i - 1] + pre[i]

            result.append(cur)

        return result