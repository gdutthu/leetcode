class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string=list(s)  # 将字符串转化成字符列表
        data={}         # 哈希表，统计子串中出现过得元素
        maxLength=0     # 满足要求的最长子串的长度
        left=0          # 子串的左边界下标

        for i in range(len(string)):
            if  string[i] not in data:
                data[string[i]]=i
                maxLength=max(maxLength,i-left+1)
            else:
                # 出现重复字符时，若该字符出现的下标不在当前子串的下标区间内，则只更新字符下标
                # 反之同时更新字符下标、子串的长度
                index=data[string[i]]
                if index<left:
                    data[string[i]]=i
                    maxLength=max(maxLength,i-left+1)

                else:
                    data[string[i]]=i
                    left=index+1
                    maxLength=max(maxLength,i-left+1)
        return maxLength