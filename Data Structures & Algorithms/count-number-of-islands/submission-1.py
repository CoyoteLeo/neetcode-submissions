class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0

        def bfs(start_r: int, start_c: int) -> None:
            q = deque([(start_r, start_c)])
            visited[start_r][start_c] = True  # 入隊當下立刻標記
            
            while q:
                cur_r, cur_c = q.popleft()
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if (
                        0 <= nr < rows 
                        and 0 <= nc < cols 
                        and not visited[nr][nc] 
                        and grid[nr][nc] == "1"
                    ):
                        visited[nr][nc] = True
                        q.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == "1":
                    ans += 1
                    bfs(i, j)

        return ans