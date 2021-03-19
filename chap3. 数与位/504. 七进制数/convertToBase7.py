class Solution:
    def convertToBase7(self, num: int) -> str:
        if num>=0:
            string=self.transfer(num)
            return string
        elif num<0:
            string=self.transfer(-1*num)
            string="-"+string
            return string

    def transfer(self,num):
        arr=[]
        while num>=0:
            s=num //7
            y=num % 7
            arr.append(y)
            if s==0:
                break
            num=s
        string=""
        while len(arr)>0:
            string +=str(arr.pop())
        return string