class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # step1:采用外排法进行排序，从最大值开始逆序排序
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # step2：经过上诉步骤后，至少有一个链表已经被遍历结束
        if m > 0:
            while m > 0:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        else:
            while n > 0:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1