'''

1319_Number_of_Operations_to_Make_Network_Connected

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.
You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

'''

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for fr,to in connections:
            if fr in graph:
                graph[fr].append(to)
            else:
                graph[fr] = [to]
            if to in graph:
                graph[to].append(fr)
            else:
                graph[to]=[fr]

        if len(connections)>=n-1:
            viz=set()
            num_of_clusters=0
            for i in range(0,n):
                st=[i]
                if i not in viz:
                    num_of_clusters+=1
                while(st):
                    node = st.pop()
                    if node not in viz:
                        viz.add(node)
                        if node in graph:
                            for j in graph[node]:
                                st.append(j)
            return num_of_clusters-1
        else:
            return -1