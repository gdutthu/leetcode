class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        pre=[1,1]
        for index in range(2,rowIndex+1):
            cur=[1]*(index+1)
            for i in range(1,index):
                cur[i]=pre[i-1]+pre[i]
            pre=cur
        return cur