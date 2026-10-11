package main

func merge(nums1 []int, m int, nums2 []int, n int) {

	i := 0
	j := 0
	k := 0
	nums := make([]int, m+n)

	for i < m && j < n {
		if nums1[i] < nums2[j] {
			nums[k] = nums1[i]
			i += 1
			k += 1
		} else {
			nums[k] = nums2[j]
			j += 1
			k += 1
		}
	}

	for i < m {
		nums[k] = nums1[i]
		i += 1
		k += 1
	}

	for j < n {
		nums[k] = nums2[j]
		j += 1
		k += 1
	}

	copy(nums1, nums)
}