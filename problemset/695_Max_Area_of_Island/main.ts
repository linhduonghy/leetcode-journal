function maxAreaOfIsland(grid: number[][]): number {
    
    let d = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    
    let m = grid.length;
    let n = grid[0].length;
    
    let visit: boolean[][] = [];
    for (let i = 0; i < m; ++i) {
        visit[i] = [];
        for (let j = 0; j < n; ++j) {
            visit[i][j] = false;
        }
    }
    
    let maxLand = 0; 
    for (let i = 0; i < m; ++i)
        for (let j = 0; j < n; ++j) 
            if (!visit[i][j] && grid[i][j] == 1) {
                maxLand = Math.max(maxLand, bfs(grid, i, j, m, n, visit, d));
            }
    return maxLand;
};

function bfs(grid: number[][], sr: number, sc: number, m: number, n: number, visit: boolean[][], d: number[][]): number {
    let count = 0;
    let q = [];
    q.push([sr, sc]);
    visit[sr][sc] = true;
    while (q.length > 0) {
        let t = q.shift();
        ++count;
        for (let i = 0; i < d.length; ++i) {
            let x = t[0] + d[i][0];
            let y = t[1] + d[i][1];
            if (x >= 0 && x < m && y >= 0 && y < n && !visit[x][y] && grid[x][y] == 1) {
                visit[x][y] = true;
                q.push([x, y]);
            } 
        }
    }
    return count;
}
// 1,1,0,0,0
// 1,1,0,0,0
// 0,0,0,1,1
// 0,0,0,1,1