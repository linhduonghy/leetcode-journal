package main

import (
	"fmt"
	"slices"
)

func numberOfArrays(differences []int, lower int, upper int) int {

	um := 0
	ans := slices.Max(arr)
	mi := int(1e9)
	for _, v := range arr {
		ans = max(ans, sum-mi)
		sum += v
		mi = min(mi, sum)
	}
	return max(0, upper-(lower+ans)+1)
}

func main() {
	fmt.Println(cal([]int{4, -7, -2}, 3, 5))
}
