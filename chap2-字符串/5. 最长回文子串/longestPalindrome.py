class Solution:
    def longestPalindrome(self, s: str) -> str:
        string=list(s)      # 将字符串转化为列表
        length=len(string)

        maxLength=1
        maxStr=""

        for index in range(length):

            # 情况1：回文字符串字符个数位奇数
            count=0
            while index-count>=0 and index+count<=length-1 and string[index-count]==string[index+count]:
                count +=1
            if 2*(count-1)+1>=maxLength:
                maxLength=2*(count-1)+1
                maxStr=s[index-(count-1):index+(count-1)+1]

            # 情况2：回文字符串字符个数位奇数
            count=0
            left=index
            right=index+1
            while  left-count>=0 and right+count<=length-1 and string[left-count]==string[right+count]:
                count +=1
            if 2*count>=maxLength:
                maxLength=2*count
                maxStr=s[left-(count-1):right+(count-1)+1]

        return maxStr