# 1st

from collections import deque
# 정점 개수, 간선 갯수
n, m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [[0] for i in range(n+1)]
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)
    cnt += 1

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)

print(cnt)