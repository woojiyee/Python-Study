# 아이디어
'''
안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이기에
한 칸이 a 상어와의 거리는 2, b 상어와의 거리는 4라면 그 칸의 안전 거리는 2인 것
-> 어떤 칸의 안전 거리는 그 칸과 상어들간의 거리중 가장 작은 값

각 상어 칸의 1칸 인접한(1칸 옆에있는 상어칸을 둘러싼) 칸들을 1단계 칸, 2칸 거리의 칸들을 2단계 칸이라고 하겠음
한 상어의 1단계->2단계-> ...-> 다른 상어의 1단계 순이 아니라 : 이처럼 구하면 위 문단에서 말한 예시로 안전거리가 2에서 4로 덮어쓰기 될 것임( 더 작은 값을 재할당한다 해도 그러면 또 변화된 칸과 연관 있는 칸들은 다 다시 구해야 될 것)
각 상어의 1단계들을 먼저 다 구하고 -> 각 상어의 2단계 순으로 구해야 함 : 더 작은 안전 거리가 우선시 되서 채택될 것 -> 단계가 적을 수록 안전 거리가 작을 것음 단계순으로 구하고 방문 체크를 하여 재방문을 막아서 뒤의 단계에서는 해당 칸을 재할당 못 하도록 하기
'''

# 1st
'''
from collections import deque

n,m = map(int,input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque()
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j,0))

while q:
    y,x,cnt = q.popleft()
    graph[y][x] = cnt
    visited[y][x] = 1
    # 상,상좌대각선,좌,하좌대각선,하,하우대각선,우,상우대각선
    for ny in [1,1,0,-1,-1,-1,0,1]:
        for nx in [0,-1,-1,-1,0,1,1,1]:
            if 0<= ny < n and 0<= nx < m:
                if visited[ny][nx]==0:
                    q.append((ny,nx,cnt+1))

m = 0

for i in range(n):
    m = max(m,max(graph[i]))

print(m)
'''

# 2nd


from collections import deque

n,m = map(int,input().split())

graph = [0  for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque()

dy = [1,1,0,-1,-1,-1,0,1]
dx = [0,-1,-1,-1,0,1,1,1]

for i in range(n):
    # 행의 수만 정의해놓고 인덱스를 통해 행에 요소 받가
    # 행이 한 줄로 입력되기에 split을 통해 요소로 나누고 
    # list() 함수를 이용해 각 요소를 담은 1차원 행렬을 graph i행에 대입
    graph[i] = list(map(int,input().split()))
    # graph.append(list(map(int,input().split())))
    # 윗 줄처럼 입력받을 거면 처음 graph = []로만 정의해야 함

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))
            graph[i][j] = 0
            # 다음 칸의 안전 거리는 해당 칸의 안전거리 + 1로 하여 구하기 위해 상어 있던 칸 다시 0으로 재할당
            # 상어 인접한 칸의 안전거리가 1이 되게하기 위하여
            # 상어가 있던 칸은 재방문 하지 않으니 visited도 1로 하여 방문 막기
            visited[i][j] = 1


while q:
    y,x = q.popleft()
    # 상,상좌대각선,좌,하좌대각선,하,하우대각선,우,상우대각선
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<= ny < n and 0<= nx < m:
            if visited[ny][nx] == 0:
                graph[ny][nx] = graph[y][x]+1
                q.append((ny,nx))
                visited[ny][nx] = 1

m = 0

for i in range(n):
    m = max(m,max(graph[i]))
print(m)