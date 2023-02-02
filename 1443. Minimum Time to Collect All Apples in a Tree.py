'''

'''

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, src):
            res = 0
            for child_node in graph[node]:
                if child_node != src:
                    res += dfs(child_node, node)
            if (res or hasApple[node]) and src != -1:
                return res + 2
            return res

        return dfs(0, -1)
    
