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

# 테케가 1일 땐 출력 잘 되는데 왜 테케가 1이 아니면 출력이 안 되지?

# 4th


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