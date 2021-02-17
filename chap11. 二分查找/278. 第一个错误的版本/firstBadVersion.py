# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while left<=right:
            mid=(left+right)//2
            res=isBadVersion(mid)
            if res==False:
                left=mid+1
            elif res==True:
                # 找到第一个错误的版本
                if mid>1 and isBadVersion(mid-1)==False:
                    return mid
                else:
                    right=mid-1
        return left