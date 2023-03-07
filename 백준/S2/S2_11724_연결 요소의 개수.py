# 1st
'''
from collections import deque
import sys

input = sys.stdin.readline

# 정점 개수, 간선 갯수
n, m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)
    cnt += 1



for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)

print(cnt)
'''
# 문제 예제는 잘 나오는데
# 백준서 python 3하면 시간초과 뜨고 pypy3하면 메모리 초과 뜸

# 2nd (1st 코드 변형)
'''
# (번외 방문 체크를 while q 안에 pop할 때 안 하고
# append할 때 하는 코드)

from collections import deque
import sys

input = sys.stdin.readline
# 정점 개수, 간선 갯수
n, m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)
                visited[node] = 1
    cnt += 1

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)

print(cnt)

# 문제 예제도 다른 출력이 뜸 -> 잘못된 코드
# 당연 백준도 틀렸습니다 뜸'''

# 3rd (1st 코드 변형)
# 연결 덩어리?(문제에서는 연결 요소의 개수) 체킹을
# bfs 함수 안에서 하려면 초기화는 밖에서 값 변경은 함수 안에서 해줘야해서 글로벌 선언이 필요
# 근데 차피 맨 마즈막 for문의 if문으로 인해 한 덩어리마다 bfs가 실행되는 거니까 bfs함수 안이 아닌 밖에서 bfs함수 돈 직후에
# 수를 카운트 해줘도 됨
'''
from collections import deque
import sys

input = sys.stdin.readline

# 정점 개수, 간선 갯수
n, m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
'''
# 백준 문제 예제는 잘 돌어감( 입력 예제 입력 시 출력 예제와 같은 출력이 나옴)
# 근데 1st와 같이 
# 백준서 python 3하면 시간초과 뜨고 pypy3하면 메모리 초과 뜸

# 4th

from collections import deque
import sys

input = sys.stdin.readline

# 정점 개수, 간선 갯수
n, m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)

# 이전 코드들은 노드 방문 체크를 큐에서 꺼낼 때 했음
# -> 4th는 큐에 삽입할 때 방문 체크를 함
# (python3, pypy3 둘 다 ) 백준 맞았습니다. 뜸 