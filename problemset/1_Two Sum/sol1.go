package main

import "fmt"

func main() {
	var nums = []int {3,3}
	var target = 6
	fmt.Println(twoSum(nums, target))
}

func twoSum(nums []int, target int) []int {
	
	m := make(map[int] int)
	for i := 1; i < len(nums); i++ {
		if nums[0] + nums[i] == target {
			return []int {0, i}
		}
		if m[target - nums[i]] != 0 {
			return []int {i, m[target - nums[i]]}
		}
		m[nums[i]] = i
	}

	return []int{-1, -1}
}