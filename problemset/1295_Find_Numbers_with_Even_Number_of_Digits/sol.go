package main

import "strconv"

func findNumbers(nums []int) int {

	res := 0
	for _, num := range nums {
		if len(strconv.Itoa(num))%2 == 0 {
			res += 1
		}
	}
	return res
}
