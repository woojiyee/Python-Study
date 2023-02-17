# 문제
# a가 b의 2- 친구이다
# <=>
# a와 b가 친구 or a와 친구이고 b와 친구인 c가 존재(= 공통 친구가 존재)
# 2-친구가 가장 많은 사람 == 가장 유명한 사람
# a와 b가 친구 == b아 a도 친구 == a와 a는 친구가 아니다

# 입력
# 사람의 수 n( <= 50)
# n개의 줄에 각 사람이 친구이면 y 아니면 n

# 출력
# 가장 유명한 사람의 2-친구 수 <=> 2-친구 수가 가장 많은 사람의 2-친구 수 출력

# 1st
'''
# 사람 수
n = int(input())

# 입력받은 친구 관계
graph = []
for i in range(n):
    graph.append(input())

# 2-친구 수를 구할 리스트
answer = [0]*n 

for i in range(n):
    for j in range(n):
        if graph[i][j] == "Y":
            answer[i] += 1
            for k in range(n):
                if k != i and graph[j][k] == "Y":
                    answer[i] += 1

print(max(answer))'''

#2nd
# bfs
'''
from collections import deque

# 사람 수
n = int(input())

# 입력받은 친구 관계
graph = []
for i in range(n):
    graph.append(input())

# 2-친구 수를 구할 리스트
answer = [0] * n  

def bfs(i):
    q = deque([i])
    # 젤 처음 q에 들어가는 i는 [i]가 아니라 i로 q에 들어가는 듯
    # 그래서 popleft한 x가 젤 처음만 int형으로 나오고 
    # 그 담 q.append([j])로 인하여 리스트 []로 추가되어
    # x가 list형으로 나옴 
    while q:
        x = q.popleft()
        print("x",x)
        print("x type",type(x))
        for j in range(n):
            print("visited",visited[j])
            # print("graph",graph[x][j])
            # print("x[0]",x[0])
            if i != j and visited[j] == 0 and graph[x[0]][j] == "Y":
            # TypeError: list indices must be integers or slices, not list
                q.append([j])
                answer[i] += 1
                visited[j] = 1


for i in range(n):
    visited = [0]*n
    bfs(i)

print(max(answer))
'''
# Q.근데 앞전에 deque()선언할 때 바로 첫 데이터 넣는 코드를 봤는데 왜 그건 에러가 안 떴을까?
# 3th
'''
from collections import deque

# 사람 수
n = int(input())

# 입력받은 친구 관계
graph = []
for i in range(n):
    graph.append(input())

# 2-친구 수를 구할 리스트
answer = []

def bfs(i):
    global cnt
    q = deque([i,cnt])
    print(q) # deque([0, 0])
    while q:
        x, cnt = q.popleft()
        # TypeError: cannot unpack non-iterable int object
        for j in range(n):
            if i != j and visited[j] == 0 and graph[x][j] == "Y":
                q.append([j,cnt])
                cnt += 1
                visited[j] = 1


for i in range(n):
    cnt = 0
    visited = [0]*n
    bfs(i)
    answer[i] = cnt

print(max(answer))
'''

# 4th
'''
from collections import deque

# 사람 수
n = int(input())

# 입력받은 친구 관계
graph = []
for i in range(n):
    graph.append(input())

# 2-친구 수를 구할 리스트
answer = [0] * n  

def bfs(i):
    q = deque()
    q.append([i])
    while q:
        x = q.popleft()
        print("x",x)
        print("x type",type(x))
        for j in range(n):
            print("visited",visited[j])
            # print("graph",graph[x][j])
            # print("x[0]",x[0])
            if i != j and visited[j] == 0 and graph[x[0]][j] == "Y":
            # TypeError: list indices must be integers or slices, not list
                q.append([j])
                answer[i] += 1
                visited[j] = 1


for i in range(n):
    visited = [0]*n
    bfs(i)

print(max(answer))
'''

#5th
'''
from collections import deque

# 사람 수
n = int(input())

# 입력받은 친구 관계
graph = []
for i in range(n):
    graph.append(input())

# 2-친구 수를 구할 리스트
answer = [0] * n  

def bfs(i):
    # q = deque(i) # TypeError: 'int' object is not iterable
    q = deque([i])
    visited[i] = 1
    while q:
        x = q.popleft()
        print("x",x)
        print("x type",type(x))
        for j in range(n):
            print("visited",visited[j])
            # print("graph",graph[x][j])
            # print("x[0]",x[0])
            if i != j and visited[j] == 0 and graph[x][j] == "Y":
            # TypeError: list indices must be integers or slices, not list
                q.append(j)
                answer[i] += 1
                visited[j] = 1


for i in range(n):
    visited = [0]*n
    bfs(i)

print(max(answer))
'''
# 백준 예제4 n이 10일 때 오답이 출력됨
# 백준 틀렸습니다.

#6th

from collections import deque

# 사람 수
n = int(input())

# 입력받은 친구 관계
graph = []
for i in range(n):
    graph.append(input())

# 2-친구 수를 구할 리스트
answer = [0] * n  

def bfs(i):
    q = deque()
    q.append([i,0])
    while q:
        x, level = q.popleft()
        for j in range(n):
            if i != j and visited[j] == 0 and graph[x][j] == "Y" and level < 2:
                q.append([j,level+1])
                answer[i] += 1
                visited[j] = 1
                


for i in range(n):
    visited = [0]*n
    bfs(i)

print(max(answer))

# 백준 맞았습니다.
# 5th 차이
# 문제에서 2-친구는 공통 친구가 있는 친구도 해당
# 한 사람만 거쳐서 아는 사람만 해당 여러 사람을 거치면 안 됨
# 근데 5th같은 경우는 친구의 친구의 친구기만 하면 즉, 계속 이어지기만 하면 두단계 건너서 친구인 경우도 2-친구로 계산
# 그래서 친구를 거쳐야 되는 2-친구를 구할 때 거치는 횟수를 제한함(한다계만 거쳐서 나오는 사람만 2-친구로 인정)

