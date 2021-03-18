import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # 基本思路：其实就是求最大因数
        if area<=2:
            res=[1,area]

        res=[area,1]
        for width in range(2,int(math.sqrt(area))+1):
            if area % width==0:
                l=max(area//width,width)
                w=min(area//width,width)
                res=[l,w]
        return res