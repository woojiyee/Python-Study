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

# print(answer) # 백준 문제에서 원하는 출력이 아니어서 "틀렸습니다" 뜸

for i in answer:
    for j in i:
        print(j,end=" ")
    print()

# 백준 "맞았습니다"

# 3th
# 2nd를 수정
# answer을 따로 안 만들어도 visited만으로도 가능

from collections import deque

# 정점의 개수
n = int(input())

# 입력받는 인접 행렬 그래프
graph = [[] for i in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))


def bfs(node):
    q = deque([node])
    while q:
        now = q.popleft()
        for i in range(n):
            if graph[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)


# 정점마다 갈 수 있는 정점 루트 다 돌기
for i in range(n):
    visited = [0] * n
    bfs(i)
    for j in range(n):
        print(visited[j],end=' ')
    print()