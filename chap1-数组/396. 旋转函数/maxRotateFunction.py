class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if A == []:
            return 0
        length = len(A)
        # step1：计算F(0)
        maxValue = float("-inf")
        cur_value = 0
        for index in range(length):
            cur_value += index * A[index]
        maxValue = max(maxValue, cur_value)

        # step2:根据F(n+1)-F(n)=sum(A)-n*Bk(n-1)，计算F(n)

        arr_sum = sum(A)
        for k in range(1, length):
            cur_value = cur_value + arr_sum - length * A[-k]
            maxValue = max(maxValue, cur_value)
        return maxValue