# 1st
# 문제
'''
직사각형이 주어지면 직사각형이 없는 부분이 몇개의 영역으로 나뉜다
-> 그랬을때, 영역의 개수, 각 영역의 넓이를 출력'''
# 아이디어
'''
입력받는 직사각형이 벽인셈
직사각형이 없는 부분만 bfs를 돌리기
'''


from collections import deque

# 눈금 간격 m*n, 직사각형의 개수
# m = 행의 수 = y
# n = 열의 수 = x
m, n, k = map(int,input().split())

# 직사각형이 있는 곳과 없는 곳을 구분할 리스트
#graph = [[True]* n for i in range(m)]

# 직사각형이 없는 부분을 돌 때 방문 체크할 리스트
visited = [[0]* n for i in range(m)]

# 상하좌우로 이동할 때 쓸 리스트
dy = [1,-1,0,0]
dx = [0,0,-1,1]

# 영역 개수
cnt = 0
# 각 영역당 넓이
w = []

for i in range(k):
    LeftBottomX, LeftBottomY, RightTopX, RightTopY = map(int,input().split())

    # 첨엔 range(LeftBottomX, RightTopX +1)함
    # -> visited함수도 그렇고 0부터 시작해서 i번째 원소는 i-1인덱스를 가지는 상태로 코드를 짰으니
    # 여기서도 따로 +1 안 해줘도 됨
    for i in range(LeftBottomX, RightTopX):
        for j in range(LeftBottomY, RightTopY):
            #graph[j][i] = False
            visited[j][i] = 1

def bfs(start):
    w = 0
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    while q:
        y, x = q.popleft()
        w += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 모눈종이의 범위 안일 때만 돌리겠다!
            if 0 <= ny < m and 0<= nx < n:
                # 막혀있지 않을 때 (직사각형이 없는 부분)
                #if graph[ny][nx] == True:
                    # 첫 방문일 때만
                    if visited[ny][nx] == 0:
                        q.append((ny,nx))
                        visited[ny][nx] = 1
    return w

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            w.append(bfs((i,j)))
            cnt += 1

# 문제에서 넓이 오름차순으로 출력
w.sort()

print(cnt)
for i in w:
    print(i, end = ' ')

# 처음엔 직사각형 유뮤 리스트와 방문 유뮤 리스트를 별도로 선언하고 코드 작성
# 근데 걍 결국엔 직사각형 있는 부분도 방문을 안 하겠단 의미니 
# 직사각형 있는 부분을 방문 못하게 visited값을 1로 두면 됨
# 직사각형 유무 리스트 없이 방문 체킹 리스트 하나만 써서 코드 짬

# 백준 맞았습니다.
