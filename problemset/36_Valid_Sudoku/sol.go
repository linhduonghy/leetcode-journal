package main

func isValidSudoku(board [][]byte) bool {

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			for k := j + 1; k < 9; k++ {
				// check in row
				if board[i][j] == board[i][k] {
					return false
				}
				// check in col
				if board[j][i] == board[k][i] {
					return false
				}
			}
		}

	}

	return true
}
