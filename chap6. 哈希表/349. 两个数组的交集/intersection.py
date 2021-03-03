class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]    # 储存两个数组的交集
        data={}   # 哈希表，放在交集元素被重复储存
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        index1=0
        index2=0
        while index1<len(nums1) and index2<len(nums2):
            if nums1[index1]==nums2[index2]:
                if nums1[index1] not in data:
                    data[nums1[index1]]=1
                    arr.append(nums1[index1])
                index1 +=1
                index2 +=1
            elif nums1[index1]<nums2[index2]:
                index1 +=1
            else:
                index2 +=1
        return arr
