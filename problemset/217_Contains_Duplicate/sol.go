package main

import "fmt"

func main() {
	var arr = []int{1, 2, 3, 1}
	containsDuplicate(arr)
}

func containsDuplicate(nums []int) bool {
	var m = make(map[int]int)
	for i := 0; i < len(nums); i++ {
		fmt.Println(m)
		if m[nums[i]] != 0 {
			return true
		}
		m[nums[i]] = 1
	}
	return false
}
