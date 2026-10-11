/**
 Do not return anything, modify board in-place instead.
 */
 function solve(board: string[][]): void {

    let visit: boolean[][] = [];
    let d = [[0,1],[0,-1],[-1,0],[1,0]]
    let m = board.length;
    let n = board[0].length;
    for (let i = 0; i < m; ++i) {
        visit[i] = [];
        for (let j = 0; j < n; ++j)
            visit[i][j] = false;
    }
    for (let i = 0; i < m; ++i) {
        if (board[i][0] == 'O')
            dfs(i, 0, board, visit, m, n, d);
        if (board[i][n - 1] == 'O')
            dfs(i, n - 1, board, visit, m, n, d);
    }

    for (let i= 0 ; i < n; ++i) {
        if (board[0][i] == 'O')
            dfs(0, i, board, visit, m, n, d);
        if (board[m - 1][i] == 'O')
           dfs(m - 1, i, board, visit, m, n, d);
    }
    
    for (let i = 1; i < m - 1; ++i)
        for (let j = 1; j < n - 1; ++j)
            if (board[i][j] == 'O' && !visit[i][j]) 
                board[i][j] = 'X';
};

function dfs(x: number, y: number, board: string[][], visit: boolean[][], m: number, n: number, d: number[][]) {
    // console.log(x, y);
    visit[x][y] = true;
    for (let i = 0; i < 4; ++i) {
        let x1 = x + d[i][0];
        let y1 = y + d[i][1];
        if (x1 > 0 && x1 < m - 1 && y1 > 0 && y1 < n - 1 && board[x1][y1] == 'O' && !visit[x1][y1]) {
            dfs(x1, y1, board, visit, m, n, d);
        }
    }
}