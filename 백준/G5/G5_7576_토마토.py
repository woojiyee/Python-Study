# BFS

# 알고리즘
# 이 문제는 다른 문제처럼 [0][0]에서 시작해서 [n][m]까지 한 번 돌아서 끝나지 않음
# 1이 어디 있느냐에 따라 1이 있는 곳부터 익은 토마토가 번져나가기 시작
# 첫 상태에서 칸에 토마토가 익었으면 날짜가 하루 지나면 상하좌우( 범위 안인지 확인 필요 ) 토마토도 익음(변함)

# 상자엔 토마토가 있는 칸도 없는 칸도 존재
# 익은 토마토의 상하좌우에 익지 않은 토마토는 하루가 지나면 익는다

# 문제에서 주어지는 정보 
# - m : 상자 가로 크기
# - n : 상자 세로 크기 
# - -1 : 토마토가 없는 칸
# - 0 : 익지 않은 토마토
# - 1 : 익은 토마토
#1st
# 상자의 가로, 세로 칸 수

# 문제에서 원하는 출력
# 토마토들이 다 익는 최소 일수
# 저장될 때부터 모든 토마토가 익어있는 상태 : 0 출력
# 토마토가 모두 익지는 못하는 상황: -1 출력

from collections import deque

m, n = map(int,input().split())

graph = [[i for i in map(int,input().split())] for _ in range(n)]

# 토마토가 없는 칸 수
count = 0

# 걸리는 일자
date = [[0 * m] for _ in range(n)]

# 상하좌우 칸으로 이동
dy = [-1,1,0,0]
dx = [0,0,-1,1]

'''
def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= n or nx < 0 or nx > m:
                continue 
            if graph[ny][nx] == -1:
                count += 1
                continue
            # 익은 토마토면
            if graph[ny][nx] == 1:
                queue.append((ny,nx))
                date[ny][nx] = date[y][x] + 1
'''
'''
def bfs(y,x):
    # 현재 칸이 빈 경우
    if graph[y][x] == -1:
        count += 1
    # 현재 칸에 익은 토마토가 있는 경우
    if graph[y][x] == 1:
        queue = deque()
        queue.append((y,x))
        date += 1
        while queue:
            y,x = queue.popleft()
            for i in range(4):
                ny = y + dy
                nx = x + dx'''
            



def bfs(y,x):
    queue = deque()

    if graph[y][x] == -1:
        print( " 그 다음 단계 진행 ")
    if graph[y][x] == 1:
        queue.append((y,x))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx > m:
                continue
            # 하루가 지나면 상하좌우에 있는 토마토도 익음
            date[ny][nx] = date[y][x] +1
            graph[ny][nx] = 1