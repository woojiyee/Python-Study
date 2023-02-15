# bfs
from collections import deque

# 1st
'''
# 정점의 개수
n = int(input())

# 입력받는 인접 행렬 그래프
graph = [[] for i in range(n)]
for i in range(n):
    graph = list(map(int,input().split()))

# 출력할 인접 행렬 그래프
answer = [[0] for i in range(n)]

def bfs(node):
    q = deque(node)
    while q:
        now = q.popleft()
        for i in range(n):
            # 현재항에서 출발하는 간선으로 이어진 노드
            if graph[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
                answer[now][i] = 1 





# 정점마다 갈 수 있는 정점 루트 다 돌기
for i in range(n):
    visited = [0] * n
    bfs(i)

print(answer)
'''

# 2nd


# 정점의 개수
n = int(input())

# 입력받는 인접 행렬 그래프
graph = [[] for i in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

# 출력할 인접 행렬 그래프
answer = [[0 for i in range(n) ] for i in range(n)]

def bfs(node):
    q = deque([node])
    while q:
        now = q.popleft()
        for i in range(n):
            if graph[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
                answer[node][i] = 1 





# 정점마다 갈 수 있는 정점 루트 다 돌기
for i in range(n):
    visited = [0] * n
    bfs(i)

print(answer)