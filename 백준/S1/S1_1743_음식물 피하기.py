# 문제
'''
통로 중간 중간 음식물이 떨어져있다
음식물은 근처에 있는 것끼리 뭉쳐서 큰 음식물 쓰레기가 된다
떨어진 음식물 중 제일 큰 음식물만은 피해가려고 한다
제일 큰 음식물의 크기를 구해라
'''

# 1st
'''
# 통로의 세로 길이, 가로 길이, 음식물 쓰레기의 개수
n, m, k = map(int,input().split())

# 통로
g = [[0 for i in range(m+1)] for _ in range(n+1)]

visited = [[0 for i in range(m+1)] for _ in range(n+1)]

# 통로 중 음식물 쓰레기가 있는 위치 : 1
for i in range(k):
    r,c = map(int,input().split())
    g[r][c] = 1

dy = [1,-1,0,0]
dx = [0,0,-1,1]

ans = 0

def dfs(r,c):
    global size
    visited[r][c] = 1
    size += 1
    for k in range(4):
        ny = r + dy[k]
        nx = c + dx[k]
        if 1<= ny <= n and 1<= nx <= m:
            if visited[ny][nx] == 0:
                dfs(ny,nx)
            

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and visited[i][j] == 0:
            size = 1
            dfs(i,j)
            ans = max(ans,size)

print(ans)
'''
# 원하는 결과 안 나옴
# 오답

# 2nd
'''
# 통로의 세로 길이, 가로 길이, 음식물 쓰레기의 개수
n, m, k = map(int,input().split())

# 통로
g = [[0 for i in range(m+1)] for _ in range(n+1)]

visited = [[0 for i in range(m+1)] for _ in range(n+1)]

# 통로 중 음식물 쓰레기가 있는 위치 : 1
for i in range(k):
    r,c = map(int,input().split())
    g[r][c] = 1

dy = [1,-1,0,0]
dx = [0,0,-1,1]

ans = 0

def dfs(r,c):
    global size
    visited[r][c] = 1
    size += 1
    for k in range(4):
        ny = r + dy[k]
        nx = c + dx[k]
        if 1<= ny <= n and 1<= nx <= m:
            if visited[ny][nx] == 0 and g[ny][nx]==1:
                dfs(ny,nx)
            

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and visited[i][j] == 0:
            size = 0
            dfs(i,j)
            ans = max(ans,size)

print(ans)
'''

# 3rd

import sys
sys.setrecursionlimit(100000)

# 통로의 세로 길이, 가로 길이, 음식물 쓰레기의 개수
n, m, k = map(int,input().split())

# 문제에서 1<= 가로,세로 길이(n,m) 이고 입력받는 쓰레기 위치 좌표 또한 1 이상
# 입력받는 쓰레기 좌표가 0에서 시작되지 않기에 문제에서 받는 위치를 똑같이 쓰기 위해 행,열 길이를 +1 해 줌
# 통로
g = [[0 for i in range(m+1)] for _ in range(n+1)]

visited = [[0 for i in range(m+1)] for _ in range(n+1)]

# 통로 중 음식물 쓰레기가 있는 위치 : 1
for i in range(k):
    r,c = map(int,input().split())
    g[r][c] = 1

dy = [1,-1,0,0]
dx = [0,0,-1,1]

ans = 0

def dfs(r,c):
    global size
    visited[r][c] = 1
    size += 1
    for k in range(4):
        ny = r + dy[k]
        nx = c + dx[k]
        if 1<= ny <= n and 1<= nx <= m:
            if visited[ny][nx] == 0 and g[ny][nx]==1:
                dfs(ny,nx)
            
# g 리스트의 인덱스가 n,m까지 있으므로 다 돌리기 위해선 range는 +1한 값으로 돌려줘야함
for i in range(n+1):
    for j in range(m+1):
        if g[i][j] == 1 and visited[i][j] == 0:
            size = 0
            dfs(i,j)
            ans = max(ans,size)

print(ans)

# 백준 맞았습니다.
# setrecursionlimit 안 써주면 recursionError 뜸

