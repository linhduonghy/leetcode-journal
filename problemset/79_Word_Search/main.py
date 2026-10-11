class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visit = [[False for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:                    
                    visit[i][j] = True                    
                    if (self.dfs(board, word[1:], i, j, visit, m, n)):
                        return True
                    visit[i][j] = False
        return False
    
    def dfs(self, board: List[List[str]], word: str, x: int, y: int, visit: List[List[bool]], m: int, n: int) -> bool:
        if not word:     
            return True
        flag = False
        for k in [(0,1), (0,-1), (1,0), (-1, 0)]:
            nx, ny = x + k[0], y + k[1]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and not visit[nx][ny] and board[nx][ny] == word[0]:
                flag = True
                visit[nx][ny] = True
                if self.dfs(board, word[1:], nx, ny, visit, m, n):
                    return True
                visit[nx][ny] = False
        if not flag: 
            return False


