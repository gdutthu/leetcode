class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)

        # pre[i]=nums[0]*num[1]**num[i-1]
        # poster[i]=nums[i+1]*num[i+2]**num[-1]
        pre=[1]*length
        poster=[1]*length

        for index in range(1,length):
            pre[index]=pre[index-1]*nums[index-1]
        for index in range(length-2,-1,-1):
            poster[index]=poster[index+1]*nums[index+1]
        res=[0]*length
        for index in range(length):
            res[index]=pre[index]*poster[index]
        return res
