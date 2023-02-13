# 이것이 코딩 테스트다.10장 그래프 이론

# 문제
'''
(a,b)칸에서 (a',b')칸으로 이동시 나이트 이동 횟수는?
입력
테스트 케이스 개수
( 체스판의 한 변의 길이
  나이트가 현재 있는 칸의 y x 좌표
  이동하려는 칸의 y x 좌표 )
각 테케는 ( )와 같이 3줄로 이루어져있음
출력
최소 이동 횟수
'''
# 알고리즘
'''
(y,x)
상하로 2칸 이동 + 좌측 또는 우측으로 한칸 이동
또는
좌우로 2칸 이동 + 상 또는 하측으로 한칸 이동
(n,m) -> (n+_2,m+-1) or (n+-1,m+-2)'''

# 1st
'''
from collections import deque

def move(start,end,l):
    global cnt
    queue = deque()
    queue.append(start)
    while queue:
        y, x, cnt = queue.popleft()
        if y < 0 or y >= l or x <0 or x >= l:
            # 범위 밖인 경우 해당 위치의 좌표는 더 진행 안 함
            # 다른 좌표들은 계속 while문 진행 -> continue
            continue
        if [y,x] == end:
            print(cnt)
            # 원하는 답을 찾음
            # 최소 횟수가 궁금하기에 더 이상 move 함수 자체를 진행 안 해도 됨
            # 함수 끝내기
            return
        queue.append(y+2,x+1,cnt+1)
        queue.append(y+2,x-1,cnt+1)
        queue.append(y-2,x+1,cnt+1)
        queue.append(y-2,x-1,cnt+1)
        queue.append(y+2,x+1,cnt+1)
        queue.append(y+1,x+2,cnt+1)
        queue.append(y-1,x+2,cnt+1)
        queue.append(y+1,x-2,cnt+1)
        queue.append(y-1,x-2,cnt+1)

# 테스트 케이스 수
n = int(input())

for i in range(n):
    # 이동 횟수 (테스트 케이스가 바뀔 때마다 초기화 <=> for문 안에서 초기화)
    cnt = 0
    l = int(input())
    start = int(input().split())
    end = list(map(int,input().split()))
    move(start,end,l)
'''

# 2ND
'''
from collections import deque

def move(start,end,l):
    global cnt
    queue = deque()
    queue.append(start.append(cnt))
    while queue:
        y, x, cnt = queue.popleft()
        if y < 0 or y >= l or x <0 or x >= l:
            # 범위 밖인 경우 해당 위치의 좌표는 더 진행 안 함
            # 다른 좌표들은 계속 while문 진행 -> continue
            continue
        if [y,x] == end:
            print(cnt)
            # 원하는 답을 찾음
            # 최소 횟수가 궁금하기에 더 이상 move 함수 자체를 진행 안 해도 됨
            # 함수 끝내기
            return
        queue.append(y+2,x+1,cnt+1)
        queue.append(y+2,x-1,cnt+1)
        queue.append(y-2,x+1,cnt+1)
        queue.append(y-2,x-1,cnt+1)
        queue.append(y+2,x+1,cnt+1)
        queue.append(y+1,x+2,cnt+1)
        queue.append(y-1,x+2,cnt+1)
        queue.append(y+1,x-2,cnt+1)
        queue.append(y-1,x-2,cnt+1)

# 테스트 케이스 수
n = int(input())

for i in range(n):
    # 이동 횟수 (테스트 케이스가 바뀔 때마다 초기화 <=> for문 안에서 초기화)
    cnt = 0
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    move(start,end,l)
'''
# while문 안에서 y,x 범위 체크를 안 하고 일단 큐에 추가 후 범위 체크를 하니까 범위를 넘어서도 큐에 다 저장되서 그런지
# 메모리 초과 뜸( 파이썬 알고리즘 돌려주는 사이트에서)

# 3rd
'''
from collections import deque

def move(start,end,l):
    global cnt
    queue = deque()
    queue.append(start)
    while queue:
        y, x, cnt = queue.popleft()
        if [y,x] == end:
            #print(cnt)
            # 원하는 답을 찾음
            # 최소 횟수가 궁금하기에 더 이상 move 함수 자체를 진행 안 해도 됨
            # 함수 끝내기
            return cnt
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < l and 0 <= nx < l:
                queue.append([ny,nx,cnt +1])
        
        

# 테스트 케이스 수
n = int(input())

dy = [2,2,-2,-2,1,-1,1,-1]
dx = [1,-1,1,-1,2,2,-2,-2]

for i in range(n):
    # 이동 횟수 (테스트 케이스가 바뀔 때마다 초기화 <=> for문 안에서 초기화)
    cnt = 0
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    start.append(cnt)
    # move(start,end,l)
    print(move(start,end,l))
'''

# vscode서 테케가 1일 땐 출력 잘 되는데 왜 테케가 1이 아니면 출력이 안 되지?
# 백준에 돌리니 메모리 초과 뜸

# 4th
'''
from collections import deque

# 테스트 케이스 수
n = int(input())

dy = [2,2,-2,-2,1,-1,1,-1]
dx = [1,-1,1,-1,2,2,-2,-2]

# 체스판 길이 
l = []
# 시작 좌표 
start = []
# 도착 좌표
end = []

for i in range(n):
    l.append(int(input()))
    start.append(list(map(int,input().split())))
    end.append(list(map(int,input().split())))

def move(start,end,l):
    global cnt
    queue = deque()
    queue.append(start)
    while queue:
        y, x, cnt = queue.popleft()
        if [y,x] == end:
            print(cnt)
            # 원하는 답을 찾음
            # 최소 횟수가 궁금하기에 더 이상 move 함수 자체를 진행 안 해도 됨
            # 함수 끝내기
            return
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < l and 0 <= nx < l:
                queue.append([ny,nx,cnt +1])
        

for i in range(n):
    # 이동 횟수 (테스트 케이스가 바뀔 때마다 초기화 <=> for문 안에서 초기화)
    cnt = 0
    start[i].append(cnt)
    move(start[i],end[i],l[i])
'''
# 메모리 초과 뜸

# 5TH( 3rd 수정 feat.블로그)
# bfs 이용
'''
from collections import deque

def move(start,end,l):
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        if [y,x] == end:
            print(graph[y][x])
            # 원하는 답을 찾음
            # 최소 횟수가 궁금하기에 더 이상 move 함수 자체를 진행 안 해도 됨
            # 함수 끝내기
            return
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < l and 0 <= nx < l and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny,nx])
        
        

# 테스트 케이스 수
n = int(input())

dy = [2,2,-2,-2,1,-1,1,-1]
dx = [1,-1,1,-1,2,2,-2,-2]

for i in range(n):
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    graph = [[0]* l for _ in range(l)]
    graph[start[0]][start[1]] = 1
    move(start,end,l)
'''
# 백준 틀렸습니다가 나옴
# 4th까진 그냥 그 칸까지 오는데 이동 횟수만 기억 함
# 근데 그러면 같은 좌표를 다양한 루트로 올 수가 있나봄 
# 그랬을 때 이미 와본 좌표를 다시 확인하는 건 메모리적 시간적 낭비니까
# 첨 온 좌표인 경우만 진행하도록 bfs로 해야하나 봄
# 근데 답 나오면 멈추게 하는 코드 4th까지의 코드처럼 짜면 최소 횟수에서 안 걸리나? 같은 좌표를 다시 오지 않고 첨 왔을 때 return만나서 출력하는 거 아닌가?

#6th


from collections import deque

def move(start,end,l):
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        if [y,x] == end:
            print(graph[y][x]-1)
            # 원하는 답을 찾음
            # 최소 횟수가 궁금하기에 더 이상 move 함수 자체를 진행 안 해도 됨
            # 함수 끝내기
            return
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < l and 0 <= nx < l and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny,nx])
        
        

# 테스트 케이스 수
n = int(input())

dy = [2,2,-2,-2,1,-1,1,-1]
dx = [1,-1,1,-1,2,2,-2,-2]

for i in range(n):
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    graph = [[0]* l for _ in range(l)]
    graph[start[0]][start[1]] = 1
    move(start,end,l)

# 6th 백준에서 맞았습니다 나옴
# 5th와 다른 점 : print할 때 -1 해준 것
# 근데 왜 빼야 하는 지 몰겠음
# Q. y,x에서 한 번 더 이동해서 ny,nx로 오니까 graph[ny][nx] = graph[y][x] + 1 해 준 것 그러니 다시 돌 때 graph[y][x]값은 현재 위치까지의 이동 횟수가 맞지 않나?
# A. 첨에 graph[start[0]][start[1]]는 이동한 적 없는 시작점이니까 0이어야 맞는데 1을 대입해줌 그래서 그 이후의 graph[y][x]에는 원래 이동 수보다 1 큰 값이 들어가있음
#    그래서 정답은 1을 빼준 값으로 출력
# 근데 여기서 graph[start[0]][start[1]] = 1을 왜 해준지 몰겠음 
# 차피 graph[y][x] == 0인지를 조건으로 체크하는 건 시작점의 다음 점이라 시작점의 graph값은 체킹하는데가 없어서 의미가 없는데

# 7Th
# 6th에서 graph[start[0]][start[1]]에 따로 1을 대입 해주지 않음(그럴 필요 없으니 위에 6th 주석에 적어놓음)
# 시작값에 따로 더한 값이 없으니 출력도 따로 안 빼줘도 됨
# 그 코드를 수정한 코드

from collections import deque

def move(start,end,l):
    global cnt
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        if [y,x] == end:
            print(graph[y][x])
            # 원하는 답을 찾음
            # 최소 횟수가 궁금하기에 더 이상 move 함수 자체를 진행 안 해도 됨
            # 함수 끝내기
            return
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < l and 0 <= nx < l and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny,nx])
        
        

# 테스트 케이스 수
n = int(input())

dy = [2,2,-2,-2,1,-1,1,-1]
dx = [1,-1,1,-1,2,2,-2,-2]

for i in range(n):
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    graph = [[0]* l for _ in range(l)]
    move(start,end,l)

Q. 근데 답 나오면 멈추게 하는 코드 4th까지의 코드처럼 짜면 최소 횟수에서 안 걸리나? 같은 좌표를 다시 오지 않고 첨 왔을 때 return만나서 출력하는 거 아닌가?

