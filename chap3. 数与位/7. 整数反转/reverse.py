class Solution:
    def reverse(self, x: int) -> int:
        item=abs(x)

        #用列表结构储存数字的每个位数
        numArray=[]
        while item>=0:
            s=int(item /10)     #商
            y=int(item %10)     #余数
            numArray.append(y)
            if s==0:
                break
            item =s
        reverseNum=0   #将翻转后的数字重新组合成十进制数
        item=1
        for index in range(len(numArray)-1,-1,-1):
            reverseNum +=numArray[index]*item
            item *=10
        if x<0:
            reverseNum=reverseNum*(-1)

        if  -2147483648 < reverseNum < 2147483647:
            return reverseNum
        else:
            return 0