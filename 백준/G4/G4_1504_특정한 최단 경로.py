# 문제
'''
- 방향성이 없는 그래프
- 1번 정점에서 n번 정접으로 최단 거리 이동
- 임의로 주어진 두 정접은 반드시 통과해아함
- 최단 경로를 구하라

- 한번 이동했던 정점과 간선을 다시 이동 가능

입력
- '''

# 1st

import heapq

# 노드 개수, 간선 개수
n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    # a번 정점에서 b번 정점까지 거리가 c인 양방향 간선
    a, b, c = map(int,input().split())

    graph[a].append((c,b))
    graph[b].append((c,a))

v = [0] * 3

for i in range(1,3):
    v[i] = map(int,input().split())

def dijkstra(start):
    h = []
    heapq.heappush(h,(0,start))
    distance[start] = 0

    while h:
        d, now = heapq.heappop()
        if d > distance[now]:
            continue
        for dis, node in graph[start]:
            if d + dis < distance[node]:
                distance[node] = d + dis
                heapq.heappush(h,(d+dis,node))

INF = 1e9
distance = [INF] * (n+1)
dijkstra(1)
distance_v = [0] * 3
distance_v[1] = distance[v1]
distance_v[2] = distance[v2]

for i in range(1,3):
    distance = [INF] * (n+1)
    dijkstra(v[i])
    distance_v[i] += distance[v[]]
    
    


