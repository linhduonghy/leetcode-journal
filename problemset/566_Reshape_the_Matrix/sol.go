package main

func matrixReshape(mat [][]int, r int, c int) [][]int {
	if len(mat)*len(mat[0]) != r*c {
		return mat
	}

	// m := len(mat)
	n := len(mat[0])

	result := make([][]int, r)
	for i := range result {
		result[i] = make([]int, c)
		for j := range result[i] {
			result[i][j] = mat[(c*i+j)/n][(c*i+j)%n]
		}
	}

	return result
}
