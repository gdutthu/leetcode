class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[0]*(num+1)
        for i in range(1,num+1):
            count=self.trans(i)
            res[i]=count
        return res


    # 函数功能：统计一个十进制数num，二进制表达中数字1出现的次数
    def trans(self,num):
        count=0
        while num>=0:
            s=int(num/2)
            y=int(num % 2)

            if y==1:
                count +=1

            if s==0:
                break
            num=s
        return count