# Nth
# 우선순위 q 사용을 위해 heap을 이용할 거임 
# -> heapq 사용
import heapq
# 그냥 input으로 입력받으니 시간 초과 뜸ㅜㅜ
# sys 써야 시간 초과 안 뜸
import sys
input = sys.stdin.readline

# 정점의 개수, 간선 개수
v, e = map(int,input().split())

# 정점별 연결된 노드와 간선을 저장할 리스트
# 1부터 시작
graph = [[] for _ in range(v+1)]

# 무한한 값
INF = 1e9

print("INF 타입",type(INF))
print("INF:",INF)
print("str(INF)",str(INF))

# 시작 노드에서부터 각 노드까지의 최소 가중치를 저장할 리스트
# 원소 갯수: v+1 개
# 인덱스 : 0 ~ v
distance = [INF] * (v+1)

# 시작 정점의 노드 번호
k = int(input())

distance[k] = 0


for i in range(e):
    # u에서 v로 가는 가중치 w
    start, end, weight = map(int,input().split())
    graph[start].append((weight,end))


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dis, now = heapq.heappop(q)
        if dis > distance[now]:
            continue
        for i in graph[now]:
            if dis + i[0] < distance[i[1]]:
                distance[i[1]] = dis + i[0]
                heapq.heappush(q,(dis + i[0],i[1]))

dijkstra(k)

print("v:",v)
print("내가 distance다",distance)
for i in range(1,v+1):
    print("i는 얼마까지 도는가?",i)
    print("distance[i]",distance[i])
    if distance[i] != INF :
        print(distance[i])
    else:
        # print(str(distance[i]))
        print("INF")

# 백준 맞았습니다