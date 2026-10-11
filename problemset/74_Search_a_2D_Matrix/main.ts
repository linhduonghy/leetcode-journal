function searchMatrix(matrix: number[][], target: number): boolean {

    let row = b_search_row(matrix, target, 0, matrix.length - 1);
    
    if (row == -1) {
        return false;
    }
    // console.log(row);
    let col = b_search_col(matrix[row], target, 0, matrix[row].length - 1);
    
    return col;
};

function b_search_row(matrix: number[][], target: number, l: number, r: number) {
    
    if (l == r) {
        if (matrix[l][0] <= target && matrix[l][matrix[l].length - 1] >= target) {
            return l;
        }
        return -1;
    }
    
    let mid = (l + r) >> 1;
    
    let left = b_search_row(matrix, target, l, mid);
    let right = b_search_row(matrix, target, mid + 1, r)
    
    if (left == -1 && right == -1) {
        return -1;
    }
    if (left != -1) {
        return left;
    }
    if (right != -1) {
        return right;
    }
}

function b_search_col(row: number[], target: number, l: number, r: number): boolean {
    if (l == r) {
        if (row[l] == target) {
            return true;
        }
        return false;
    }
    
    let mid = (l + r) >> 1;
    
    return b_search_col(row, target, l, mid) || b_search_col(row, target, mid + 1, r);
}