class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while True:
            if 0<=n and n<=3:
                if n in [1,3]:
                    return True
                return False
            if n % 3!=0:
                return False
            n=n//3