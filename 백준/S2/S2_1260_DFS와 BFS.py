# 1st

from collections import deque

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n, m, v = map(int,input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

# 방문할 수 있는 정점이 여러개인 경우 정점 번호가 작은 것을 먼저 방문
# 한 노드에 연결된 노드가 여러개일 때 번호가 작은 노드부터
# 아래 함수 안에서 graph[i]를 for문 돌릴거니 graph[i]에 들어가있는 순으로 방문 될 거임
# -> graph[i]를 정렬
for i in range(1,n+1):
    graph[i].sort()

def dfs(start):
    visited[start] = 1
    print(start,end = ' ')
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        node = q.popleft()
        print(node,end = ' ')
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

visited = [0 for i in range(n+1)]

dfs(v)
print()

visited = [0 for i in range(n+1)]
bfs(v)

# 백준 맞았습니다