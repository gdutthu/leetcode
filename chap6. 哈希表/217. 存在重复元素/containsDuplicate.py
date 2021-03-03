class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data={}
        for item in nums:
            if item not in data:
                data[item]=1
            else:
                return True
        return False