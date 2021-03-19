class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #情况一：除1外，2的幂必定是偶数
        #情况二：对于一个偶数，不断的进行二分，直到这个在0~10的范围内，次数若该数为1,2,4,8.那么这个数就是2的幂数
        while n>=10:
            if n %2 !=0:
                return False
            n= n /2
        data=[1,2,4,8]
        if n in data:
            return True
        else:
            return False