import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(math.sqrt(c))+1
        while left<=right:
            item=left**2+right**2
            if item==c:
                return True
            elif item<c:
                left +=1
            elif item>c:
                right -=1
        return False
