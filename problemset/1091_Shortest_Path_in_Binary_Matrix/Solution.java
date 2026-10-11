
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) {
            return -1;
        }
        return bfs(grid, 0, 0, n - 1, n - 1, n);
    }

    private int bfs(int[][] grid, int sx, int sy, int dx, int dy, int n) {
        Queue<Point> queue = new LinkedList<>();
        int[] r = { -1, -1, -1, 0, 0, 1, 1, 1 };
        int[] c = { -1, 0, 1, -1, 1, -1, 0, 1 };
       
        queue.offer(new Point(sx, sy, 1));
        grid[sx][sy] = 1;

        while (!queue.isEmpty()) {
            Point p = queue.remove();
            if (p.x == dx && p.y == dy) {
                return p.distance;
            }
            int dis = p.distance;
            for (int i = 0; i < 8; ++i) {
                int x = p.x + r[i];
                int y = p.y + c[i];
                if (x >= 0 && y >= 0 && x < n && y < n && grid[x][y] == 0) {                    
                    queue.add(new Point(x, y, dis + 1));
                    grid[x][y] = 1;
                }
            }
        }
        return -1;
    }

    static class Point {
        int x;
        int y;
        int distance;
        public Point(int x, int y, int distance) {
            this.x = x;
            this.y = y;
            this.distance = distance;
        }

    }
}