class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            # 因为我们是直接原地修改元素为负值来标记是否访问过，因此这里的num一定要取绝对值
            index = abs(num) - 1
            val = nums[index]
            if val < 0:
                # 如果元素值为负数，说明之前存在同一个索引为num的元素
                res.append(abs(num))
            # 原地修改访问标志
            nums[index] = -nums[index]
        return res