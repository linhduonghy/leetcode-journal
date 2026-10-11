function minimumTotal(triangle: number[][]): number {

    let n = triangle.length;

    let dp: number[][] = [];

    for (let i = 0; i < n; ++i) {
        dp[i] = [];
        for (let j = 0; j < triangle[i].length; ++j) {
            dp[i][j] = 1e8;
        }
    }

    dp[0][0] = triangle[0][0];

    for (let i = 0; i < n - 1; ++i) {
        for (let j = 0; j < triangle[i].length; ++j) {
            dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + triangle[i + 1][j]);
            dp[i + 1][j + 1] = Math.min(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1]);
        }
    }

    return Math.min.apply(null, dp[n - 1]);
};