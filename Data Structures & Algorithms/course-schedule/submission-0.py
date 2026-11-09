class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = defaultdict(set)
        next_classes = defaultdict(set)

        for i, j in prerequisites:
            dependency[j].add(i)
            next_classes[i].add(j)

        queue = deque()
        for course in range(numCourses):
            # no dependency
            if course not in dependency:
                queue.append(course)
        
        while queue:
            course = queue.pop()
            for next_class in next_classes[course]:
                if course not in dependency[next_class]:
                    continue
                
                dependency[next_class].remove(course)
                if not dependency[next_class]:
                    queue.append(next_class)
        return all(not v for v in dependency.values())

        
        
