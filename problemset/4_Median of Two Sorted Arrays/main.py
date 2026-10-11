class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        merged_array = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
               
            else:
                merged_array.append(nums2[j])
                j += 1        
        while i < m:
            merged_array.append(nums1[i])
            i += 1
        while j < n:
            merged_array.append(nums2[j])
            j += 1
        print(merged_array)
        mid = (m + n + 1) // 2 - 1
        if (m + n) % 2 == 1:
            return merged_array[mid]
        else:
            return (merged_array[mid] + merged_array[mid + 1]) / 2