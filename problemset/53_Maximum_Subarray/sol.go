package main

import "fmt"

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

func maxSubArray(nums []int) int {

	var maxSum = nums[0]
	var minn = 0
	var s = 0
	for _, v := range nums {
		s += v
		maxSum = max(maxSum, s-minn)
		minn = min(minn, s)

		fmt.Println(maxSum)
	}

	return maxSum
}