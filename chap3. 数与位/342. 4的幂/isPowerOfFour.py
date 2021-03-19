class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        while True:
            if 0<=n and n<=4:
                if n in [1,4]:
                    return True
                else:
                    return False
            if n % 4 !=0:
                return False
            n= n//4