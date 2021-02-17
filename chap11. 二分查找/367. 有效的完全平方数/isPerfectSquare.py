class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=1
        right=num
        while left<=right:
            mid=(left+right)//2
            res=mid**2
            if res==num:
                return True
            elif res<num:
                left=mid+1
            elif res>num:
                right=mid-1
        return False