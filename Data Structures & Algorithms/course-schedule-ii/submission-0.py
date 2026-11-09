class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses  # 每堂課的前置數量(parents)
        adj = [[] for i in range(numCourses)]  # 這門課可以 unblock 哪些課(children)
        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        # 從沒有前置的開始
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return ans if len(ans) == numCourses else []