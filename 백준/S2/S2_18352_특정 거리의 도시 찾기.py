# 수도 코드
'''
- 단반향 거리기에 1->2, 1->3 과 같이 시작과 끝이 중요
1. 출발 번호 x를 큐에 삽입 -> popleft (해당 노드를 처음 방문하는 경우에만 거리 +1)
2. 큐 젤 앞에 있는 노드(popleft한 노드)가 시작하는 노드(0열)인 행의 1열 노드가 큐에 삽입
3. 맨 앞에 있는 노드 popleft -> popleft한 노드를 0열로 갖고 있는 1열 노드를 삽입
4. 반복
5. 최단 거리가 k인 도시들 리스트에 저장
6. 5번 리스트 오름차순 정렬
7.5번 리스트가 있으면 한줄씩 출력, 없으면 -1 출력
'''

from collections import deque

# 도시의 개수: N, 도로의 개수: M, 거리 정보: K, 출발 도시의 번호: X를 공백으로 구분하여 입력받기
n, m, k, x = map(int, input('도시 개수, 도로 개수, 최단 거리, 출발 도시 번호 입력:').split())
# 2차원 리스트의 맵 정보 입력받기
before = []
# 리스트[n]= [n 노드에서 갈 수 있는 노드]
graph = [[] for _ in range(n+1)]
# 각 노드별 방문 여부
visited = [False] * (n+1)
# 이동 거리 ( 시작 노드를 popleft할 땐 이동 거리를 치면 안 되고 그 담부터 쳐야해서 초기값을 -1로)
# 다른 노드로 가면 ( 도로가 갈리면) 이동 거리를 따로 세야하기에 리스트로 구분
distance = [-1] * (n+1)

print('graph',graph)
for i in range(m):
    before.append(list(map(int,input("도로 입력:").split())))

# 거리(a 도시-> b 도시) 행의 시작 노드가 i면 graph[i]에 도착 노드 추가
for i in range(1,n+1):
    for j in range(m):
        if before[j][0] == i:
            graph[i].append(before[j][1])

print("graph:",graph)

# BFS 소스 코드 구현
def bfs(start):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:        
        i = queue.popleft()
        print('빼는 노드:',i)
        # 한 노드를 뺄 때마다 다른 노드로 이동한거니 이동 거리 +1
        global distance
        print("거리 증가 전 distance[",i,"]:",distance[i])
        distance[i] += 1
        print("거리 증가 후 distance[",i,"]:",distance[i])
        # 해당 원소와 연결된 노드 중 방문 기록이 없는 노드들을 큐에 삽입
        for j in graph[i]:
            if visited[j] != True:
                queue.append(j)
                visited[j] = True
                # 그 전 이동거리로 재할당
                distance[j] = distance[i]

'''# BFS를 수행한 결과 출력
print(bfs(0,0))'''

'''for i in range(n):
    # 0열에 시작 노드가 있는 경우 -> 인접 노드는 1열
    if graph[i][0] == x :
        bfs(i,1)
    elif graph[i][1] == x :
        bfs(i,0)'''

bfs(x)

distance.sort()

print("distance:",distance)
if k in distance:
    for i in range(len(distance)):
        if k == distance[i]:
            print(i)
    
else:
    print(-1)
    

# 이코테 교제 참조... 여러번 시도해서 품 과정 다 안 적음



