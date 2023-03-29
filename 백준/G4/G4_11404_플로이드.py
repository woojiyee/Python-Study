# 1st
import heapq
# 그냥 input으로 입력받으니 시간 초과 안 뜨지만 채점 하는 데 엄청 걸림
# sys 쓰니 바로 정답 결과 나옴
import sys
input = sys.stdin.readline

# 도시 개수
n = int(input())

# 버스 개수
m = int(input())

graph = [[] for i in range(n+1)]

# 무한한 값
INF = 1e9

answer = [[] for i in range(n+1)]

for i in range(m):
    # 버스 시작 도시, 도착 도시, 한 번 타는데 필요한 비용 
    a, b, c = map(int,input().split())
    graph[a].append((c,b))

def dijkstra(start):
    h = []
    heapq.heappush(h,(0,start))
    distance[start] = 0

    while h:
        nowDis, now = heapq.heappop(h)
        if nowDis > distance[now]:
            continue
        for dis, node in graph[now]:
            if nowDis + dis < distance[node]:
                distance[node] = nowDis + dis
                heapq.heappush(h,(nowDis+dis, node))
    return distance

for i in range(1,n+1):
    # 시작 노드에서부터 각 노드까지의 최소 가중치를 저장할 리스트
    # 원소 갯수: v+1 개
    # 인덱스 : 0 ~ v
    distance = [INF] * (n+1)
    answer[i] = dijkstra(i)

for i in range(1,n+1):
    for j in range(1,n+1):
        if answer[i][j] < INF:
            print(answer[i][j],end = ' ')
        else:
            print(0,end = ' ')
    print()


# 맞았습니다