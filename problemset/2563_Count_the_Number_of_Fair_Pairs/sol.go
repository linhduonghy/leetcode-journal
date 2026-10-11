package main

import "sort"

func countFairPairs(nums []int, lower int, upper int) int64 {
	sort.Ints(nums)
	return countPairs(nums, upper+1) - countPairs(nums, lower)
}

func countPairs(nums []int, value int) int64 {
	left, right := 0, len(nums)-1
	var sum int
	var count int64 = 0
	for left < right {
		sum = nums[left] + nums[right]
		if sum < value {
			count += int64(right - left)
			left += 1
		} else {
			right -= 1
		}
	}
	return count
}
