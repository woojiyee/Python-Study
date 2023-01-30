from collections import deque
import sys

# 도시의 개수: N, 도로의 개수: M, 거리 정보: K, 출발 도시의 번호: X를 공백으로 구분하여 입력받기
n, m, k, x = map(int, sys.stdin.readline().split())
# 리스트[n]= [n 노드에서 갈 수 있는 노드]
graph = [[] for _ in range(n+1)]
# 이동 거리 ( 시작 노드를 popleft할 땐 이동 거리를 치면 안 되고 그 담부터 쳐야해서 초기값을 -1로)
# 다른 노드로 가면 ( 도로가 갈리면) 이동 거리를 따로 세야하기에 리스트로 구분
distance = [-1] * (n+1)

for _ in range(m):
    first, last =  map(int, input().split())     
    graph[first].append(last)


# 큐 구현을 위해 deque 라이브러리 사용
queue = deque([x])
# 큐가 빌 때까지 반복
while queue:        
    i = queue.popleft()
    # 해당 원소와 연결된 노드 중 방문 기록이 없는 노드들을 큐에 삽입
    distance[i] += 1
    for j in graph[i]:
        if distance[j] == -1:
            queue.append(j)
            # 그 전 이동거리로 재할당
            distance[j] = distance[i]


distance.sort()

if k in distance:
    for i in range(len(distance)):
        if k == distance[i]:
            print(i)
else:
    print(-1)
