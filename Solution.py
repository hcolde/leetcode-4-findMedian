class Solution:
    
    def getMedian(self, nums):
        if len(nums) == 1:
            return nums[0]
        mid_num = len(nums) / 2
        if mid_num > int(mid_num):
            return float(nums[int(mid_num)])
        else:
            return (nums[int(mid_num) - 1] + nums[int(mid_num)]) / 2.0
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= 0:
            return self.getMedian(nums2)
        elif len(nums2) <= 0:
            return self.getMedian(nums1)
        
        nums1, nums2 = (nums1, nums2) if nums1[-1] < nums2[-1] else (nums2, nums1)
        nums1_len, nums2_len = len(nums1), len(nums2)
        new_nums = []
        i, j = 0, 0
        while i < nums1_len:
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 <= n2:
                new_nums.append(n1)
                i += 1
            else:
                new_nums.append(n2)
                j += 1
        if j < nums2_len:
            new_nums += nums2[j:]
        
        return self.getMedian(new_nums)
