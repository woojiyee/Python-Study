# 1st

import sys
sys.setrecursionlimit(10000)
n = int(input())

art = []
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    art.append(list(input()))

dy = [-1,1,0,0]
dx = [0,0,-1,1]

normal = 0
special = 0

def nor(r,c):
    visited[r][c] = 1
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if 0<= ny < n and 0 <= nx < n:
            if visited[ny][nx] == 0:
                if art[r][c] == art[ny][nx]:
                    nor(ny,nx)

def spe(r,c):
    visited[r][c] = 1
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if 0<= ny < n and 0 <= nx < n:
            if visited[ny][nx] == 0:
                if art[r][c] == "R" or art[r][c] == "G":
                    # if art[ny][nx] ==  "R" or "G":라고 짰을 때 art[ny][nx]가 B인 경우도 if문 실행되서 if 안에 명령문 실행됨
                    # 논리형 연산자를 잘못 썼어도 차라리 if 절이 실행 안 됬어야하는 거 아닌가?
                    if art[ny][nx] ==  "R" or art[ny][nx] == "G":
                        spe(ny,nx)
                elif art[r][c] == art[ny][nx]:
                    spe(ny,nx)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            nor(i,j)
            normal +=1

visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            spe(i,j)
            special +=1

print(normal,special)

# 백준 맞았습니다.