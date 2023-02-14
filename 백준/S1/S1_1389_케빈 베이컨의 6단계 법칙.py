# bfs

# 알고리즘도 모르겠고 코드도 어케 짜야하는지 몰겠다 ㅠ

# 블로그 참고

from collections import deque

# bfs 탐색
def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        target = q.popleft()

        # 친구 관계를 확인
        for i in graph[target]:
            # 탐색하지 않은 친구라면 탐색
            if not visited[i]:
            # visited[i]가 0이 아닐 때
            # visited[i] : True
            # not visited[i] : False
            # if의 조건이 참일 때만 if문이 실행되니까
            # visited[i]가 0이 아니면 실행되지 않음
            # visited[i]가 0일 떄
            # not False = True 이므로 실행됨
                # 탐색하기 위한 횟수를 체크한다
                visited[i] = visited[target] + 1
                q.append(i)

# 유저의 수, 친구 관계의 수
n, m = map(int,input().split())

# 2차원 그래프
# 유저별 입력으로 받는 1단계 친구 관계 리스트
#  범위가 n+1인 이유: 노드의 번호를 0이 아닌 1부터 시작할거기 때문
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    # a b가 친구 관계라면 
    # a의 친구 목록인 graph[a]에도 b가 있어야하고
    # b의 친구 목록인 graph[b]에도 a가 있어야하므로 
    # 서로를 서로의 그래프에 추가
    graph[a].append(b)
    graph[b].append(a)

# 케빈 베이컨의 수를 담는 리스트
res = [[] for _ in range(n+1)]

# 반복문을 통해 모든 친구를 탐색
for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs(i)
    res[i] = [sum(visited)]
    # res[i]는 1차원 배열 sum(visited)는 정수이니 []로 만들어줘서 대입
    # 아님 res[i].append(sum(visited))도 가능

# 가장 작은 케빈 베이컨 수를 가지고 있는 사람의 인덱스 출력한다
print(res.index(min(res[1:])))
# res[0]에는 값을 넣은적이 없음 
# 우린 res[1]에서부터 값을 넣었기에 인덱스 1 이후부터 유의미 최소값도 res의 인덱스 1~끝까지 중 최소값인 것을 골라야 함

# 백준에서 맞았습니다