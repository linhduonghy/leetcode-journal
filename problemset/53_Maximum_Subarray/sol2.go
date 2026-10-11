package main

func main() {
	var arr = []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	maxSubArray(arr)
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

// Kanade Algorithm
func maxSubArray(nums []int) int {

	var bestMax = nums[0]
	var curMax = nums[0]
	for _, value := range nums {
		curMax = max(curMax+value, value)
		bestMax = max(bestMax, curMax)
	}

	return bestMax
}