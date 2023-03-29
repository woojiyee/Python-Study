# 1st (bfs 버전)
'''
from collections import deque

# 컴퓨터 수
n = int(input())

# 컴퓨터 연결 수
m = int(input())

# 인덱스를 1부터 시작
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
# visited = [[0] for i in range(n+1)] 
# 이렇게 썼더니 visited [[0],[0],..]로 되서
# bfs 안 if문에서 if visited[i] != 0에서 [0] 은 0이 아니기에 다 continue 처리 됨 

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        visited[node] = 1
        for i in graph[node]:
            if visited[i] != 0:
                continue
            q.append(i)

bfs(1)            
answer = visited.count(1)

# 시작하는 노드는 감염된 노드로 치지 않는데
# 시작하는 노드도 bfs 안 while문에서 visited = 1로 처리되어 count됨 -> -1 해주기
print(answer - 1)'''

# 백준 맞았습니다.

# 2nd (dfs 버전)

# 컴퓨터 수
n = int(input())

# 컴퓨터 연결 수
m = int(input())

# 인덱스를 1부터 시작
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
# visited = [[0] for i in range(n+1)] 
# 이렇게 썼더니 visited [[0],[0],..]로 되서
# bfs 안 if문에서 if visited[i] != 0에서 [0] 은 0이 아니기에 다 continue 처리 됨 

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    if visited[node] == 0:
        visited[node] = 1
        for i in graph[node]:
            dfs(i)

dfs(1)

answer = visited.count(1)

# 시작하는 노드는 감염된 노드로 치지 않는데
# 시작하는 노드도 bfs 안 while문에서 visited = 1로 처리되어 count됨 -> -1 해주기
print(answer - 1)

# 백준 맞았습니다.

# 3rd (bfs)
# 1st에서 방문체크 순서?만 다른 코드

from collections import deque

# 컴퓨터 수
n = int(input())

# 컴퓨터 연결 수
m = int(input())

# 인덱스를 1부터 시작
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
# visited = [[0] for i in range(n+1)] 
# 이렇게 썼더니 visited [[0],[0],..]로 되서
# bfs 안 if문에서 if visited[i] != 0에서 [0] 은 0이 아니기에 다 continue 처리 됨 

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if visited[i] != 0:
                continue
            q.append(i)
            visited[i] = 1

bfs(1)            
answer = visited.count(1)

print(answer - 1)

# 백준 맞았습니다 뜸
# 1st는 큐에서 팝할 때 방문 체크
# 3rd는 큐에 추가할 때 방문 체크
# 둘 다 맞다고 뜨는데 3rd 코드 돌아가는 시간이 더 짧음.