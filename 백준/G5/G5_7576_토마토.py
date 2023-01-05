# BFS
# 다시 풀어보기!

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
'''
from collections import deque

m, n = map(int,input("상자 가로 세로 입력:").split())

graph = [[i for i in map(int,input("칸 정보 입력:").split())] for _ in range(n)]

# 토마토가 없는 칸 수
count = 0

# 걸리는 일자
date = [[0 * m] for _ in range(n)]

# 상하좌우 칸으로 이동
dy = [-1,1,0,0]
dx = [0,0,-1,1]

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
                nx = x + dx
'''         
'''
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
'''

# 익은 토마토의 상하좌우 토마토는 하루가 지나면 익어야한다 -> 또 하루가 지나며 그 익은 토마토의 주위 토마토도 익는다
# -> 근데 영향을 받아서 익은 토마토는 칸의 값을 1로 바꿔야하나? 아님 그냥 큐에 넣음으로써 익었단 의미가 되는건가?
# 최소 일자니까 한번 익은 토마토를 재방문한 루트는 날짜 체킹을 할 필요 없다. 
# (미로 문제처럼 같은 칸에 첫방문이 아니고 재방문이면 재방문 이후로의 루트는 첫방문과 같을거고 첫방문했던 루트가 더 단기간일 테니까)
# Q. 시작과 끝 칸이 정해져있는 게 아닌데 언제 도는 걸 멈춰야하지?
# 방문 체킹하는 리스트를 따로 만들지 않고 입력받은 리스트를 이용할 수 있나?
# -> 토마토 -1,1,0 리스트는 토마토 여부만 있어야 큐에 넣을지 말지를 판단하니 바꾸면 안 될거

# n회차 3번 이상 수정...
'''
from collections import deque

m, n = map(int,input("상자 가로 세로 입력:").split())

graph = [[i for i in map(int,input("칸 정보 입력:").split())] for _ in range(n)]

print("graph",graph)
# 걸리는 일자
date = [[0] * m for _ in range(n)]
print("date:",date)


# 상하좌우 칸으로 이동
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    print("bfs에 들어온 y,x",y,x)
    queue = deque()
    queue.append((y,x))
    while queue:
        print("pop 전:",queue)
        y,x = queue.popleft()
        print("pop 후:",queue)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            # 현재 칸이 빈 경우
            if graph[ny][nx] == -1:
                continue
            # 재방문인 경우
            if date[ny][nx] != 0:
                continue
            # bfs밖 for문의 if문에서 1인 칸의 y,x값이 큐에 들어감
            # 그 칸의 상하좌우 토마토들이 (위차가 범위를 벗어나지 않고 비어있지만 않다면) 하루가 지나고 익어야 함
            graph[ny][nx] = 1
            queue.append((ny,nx))
            date[ny][nx] = date[y][x] + 1   
            print("date[",ny,"][",nx,"]:",date[ny][nx])


for i in range(n):
    check = [False] * n
    if 0 in graph[i]:
        check[i] = True


# 모든 행에 0이 없을 때 = 안 익은 토마토가 없다 -> 모든 토마토가 이미 다 익어있는 상태이다
if True not in check:
    print("0")
# 0이 한개라도 있을 때
else:
    print("0이 있음 -> if문 실행")
    # 상자에 있는 모든 칸을 다 돌림
    for y in range(n):
        for x in range(m):
            # 익은 토마토가 있는 칸부터 시작
            if graph[y][x]==1:
                print("돌아감,y,x",y,x)
                bfs(y,x)
    # bfs를 다 돌려서 익을 수 있는 토마토는 다 익게 함
    # 근데도 안 익은 토마토가 있다면 애초에 처음 저장된 토마토 위치 구성이 익지 못하는 조건이었던 것
    check2 = [False] * n
    for i in range(n):
        print("graph:",graph)
        if 0 in graph[i]:
            check2[i] = True
            print("check2[",i,"]:",check2[i])
    print("check2:",check2)
    if True in check2:
        print("-1")
    else:
        list = [0] * n
        # 재방문 안 되게 했으니 날짜 젤 큰 값이 최단 기간인 것
        for j in range(n):
            list[j] = max(date[j])
        print(max(list))
'''          
# 문제의 예는 다 잘 돌아가는데 왜 백준은 틀렸다고 할까...

# 블로그

# bfs 특 queue 사용하기
# deque 모듈 안쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함)
from collections import deque

m, n = map(int, input().split())
# 토마토 받아서 넣기. 이차원 리스트로 만들어질거.
matrix = [list(map(int, input().split())) for _ in range(n)]
# 좌표를 넣을거니까 []를 넣자.
queue = deque([])
# 방향 리스트. [dx[0], dy[0]]은 곧 [-1, 0]이고 이는 왼쪽으로 이동하는 위치이다.
# 그려보면 이해하기 편함
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# 정답이 담길 변수
res = 0

# queue에 처음에 받은 토마토의 위치 좌표를 append 시킨다
# n과 m을 사용하는걸 헷갈리지 말아야 함!
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

# bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while queue:
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = queue.popleft()
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)


       
