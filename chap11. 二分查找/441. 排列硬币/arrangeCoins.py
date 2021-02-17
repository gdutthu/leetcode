class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<=1:
            return n
        index=1
        while n>0:
            if n>=index:
                n -=index
                index +=1
            else:
                break
        return index-1