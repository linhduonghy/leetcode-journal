function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {

    let d = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    
    let m = image.length;
    let n = image[0].length;
    
    let q = [];
    let visit: boolean[][] = [];
    for (let i = 0; i < m; ++i) {
        visit[i] = [];
        for (let j = 0; j < n; ++j) {
            visit[i][j] = false;
        }
    }
    
    q.push([sr, sc]);
    visit[sr][sc] = true;
    while (q.length > 0) {
        let t = q.shift();
        for (let i = 0; i < d.length; ++i) {
            let x = t[0] + d[i][0];
            let y = t[1] + d[i][1];
            if (x >= 0 && x < m && y >= 0 && y < n && !visit[x][y] && image[x][y] == image[sr][sc]) {
                visit[x][y] = true;
                image[x][y] = newColor;
                q.push([x, y]);
            } 
        }
    }
    image[sr][sc] = newColor;
    return image;
};