# BFS 문제

#1st 이코테 코드 참고함!
from collections import deque

# 미로의 가로,세로 칸 수
n,m = map(int,input("미로 크기:").split())
# 미로 영어로 : maze
maze = [[] for _ in range(n)]

# 방문 확인용 리스트
visited = [False * m] * n

print("초기화된 방문 확인 리스트:",visited)

print("빈 리스트 maze:",maze) # [[], []]

for i in range(n):
    maze[i] = list(map(int,input("미로 가로 한 줄씩 입력:")))

print("값 대입 후 리스트 maze:",maze) # [[1, 2, 3], [4, 5, 6]]

# 이동할 네 방향 (상,하,좌,우)
# 행렬은 y값 즉, 행이 아래로 갈 수록 인덱스가 커짐
# 젤 첫행이 0행, 두번째 행이 1행 -> 하로 이동이 인덱스가 +가 되고 상으로 이동이 -인 셈
dy = [-1,1,0,0]
dx = [0,0,-1,1]
# list[ny][nx] += list[dy][dx]인 셈이라 [-1,0]이동 [1,0] 이동 처럼 dy,dx가 세트로 적용됨

def bfs(y,x):
    # 큐 구현을 위해 deque 라이브러리 이용
    queue = deque()
    queue.append((y,x))
    while queue:
        y, x = queue.popleft()
        print("popleft 했을 때:",y,x)
        # 상하좌우로 이동
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 미로 범위 안인 경우만 계속 진행
            if 0 <= ny < n and 0 <= nx < m:
                # 미로 길이 없는 경우 다음 칸?으로 넘기기
                if maze[ny][nx] == 0:
                    continue
                # 해당 노드가 첫방문일 때만 최단 거리 기록
                if maze[ny][nx] == 1:
                    maze[ny][nx] = maze[y][x] + 1
                    queue.append((ny,nx))
    # 도착 지점까지의 최단 거리 반환
    return maze[n-1][m-1]

print(bfs(0,0))

