class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = [[False] * c for _ in range(r)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        q = deque()

        def _explore(_q):
            while _q:
                cur_r, cur_c = q.pop()
                if visited[cur_r][cur_c] or grid[cur_r][cur_c] != "1":
                    continue
                
                visited[cur_r][cur_c] = True
                for d in directions:
                    next_r, next_c = cur_r + d[0], cur_c + d[1]
                    if 0 <= next_r < r and 0 <= next_c < c:
                        _q.append((next_r, next_c))

        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == "1":
                    q.append((i, j))
                    ans += 1
                    _explore(q)

        return ans