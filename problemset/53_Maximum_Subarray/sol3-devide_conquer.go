package main

func main() {
	var arr = []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	maxSubArray(arr)
}

// Divide and Conquer Approach
func maxSubArray(nums []int) int {
	return maxSubArrayInRange(nums, 0, len(nums)-1)
}

func maxSubArrayCrossRange(nums []int, l int, r int, m int) (result int) {
	// find max contiguous subarray (x, mid) | x = [left -> mid]
	maxSumLeft := nums[m]
	sum := 0
	for i := m; i >= l; i-- {
		sum += nums[i]
		maxSumLeft = max(maxSumLeft, sum)
	}
	// find max contiguous subarray (mid, x) | x = [mid, right]
	maxSumRight := nums[m+1]
	sum = 0
	for i := m + 1; i <= r; i++ {
		sum += nums[i]
		maxSumRight = max(maxSumRight, sum)
	}
	result = max(maxSumLeft+maxSumRight, max(maxSumLeft, maxSumRight))
	return
}

func maxSubArrayInRange(nums []int, l int, r int) int {
	if l == r {
		return nums[l]
	}
	mid := (l + r) / 2
	result := max(maxSubArrayInRange(nums, l, mid),
		max(maxSubArrayInRange(nums, mid+1, r), maxSubArrayCrossRange(nums, l, r, mid)))
	return result
}

func min(x int, y int) int {
	if x > y {
		return y
	}
	return x
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}
