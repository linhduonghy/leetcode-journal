package main

func generate(numRows int) [][]int {

	result := make([][]int, numRows)

	result[0] = make([]int, 1)
	result[0][0] = 1

	var i = 0
	var j = 0
	for i = 1; i < numRows; i++ {
		result[i] = make([]int, i)
		result[i][0] = result[i-1][0]
		result[i][i] = result[i-1][i-1]
		for j = 1; j < i; j++ {
			result[i][j] = result[i-1][j] + result[i-1][j-1]
		}
	}

	return result
}