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
'''
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
distance_v[1] = distance[v[1]]
distance_v[2] = distance[v[2]]

for i in range(1,3):
    distance = [INF] * (n+1)
    dijkstra(v[i])
    if i == 1:
        distance_v[i] += distance[v[2]]
    else:
        distance_v[i] += distance[v[1]]
'''   

# 2nd ( 블로그 참고 )
# 두 노드 경유하면서 최단 거리
# 2가지 경우
# start -> v1 -> v2 -> end
# start -> v2 -> v1 -> end
# 둘 중 최소값

import heapq

# 노드 개수, 간선 개수
n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    # a번 정점에서 b번 정점까지 거리가 c인 양방향 간선
    a, b, c = map(int,input().split())

    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int,input().split())

INF = 1e9


def dijkstra(start):
    distance = [INF] * (n+1)
    # 파이썬에서 리스트는 전역변수 아닌가?
    # 그래서 따로 global 선언 안 해줘도 함수 안에서 값 재할당 되면
    # 밖에 리스트도 같이 변경됐지않나?
    # 근데 이렇게 하면 밖에 distance[]에 영향을 안 줌 
    # 함수 밖에서 distance[] = []라고 선언시, 런타임 에러 (IndexError) 뜸
    # 함수 밖에서 distance[] = [INF] * (n+1)로 초기화시, 틀렸습니다 뜸
    # 함수 안에서 재할당 전 global distance 해주면 맞았습니다 뜸
    h = []
    heapq.heappush(h,(0,start))
    distance[start] = 0

    while h:
        d, now = heapq.heappop(h)
        if d > distance[now]:
            continue
        for dis, node in graph[now]:
            if d + dis < distance[node]:
                distance[node] = d + dis
                heapq.heappush(h,(d+dis,node))


distance = []
dijkstra(1)
distance_v1 = distance[v1]
distance_v2 = distance[v2]

dijkstra(v1)
distance_v1 += distance[v2]
distance_v2 += distance[n]

dijkstra(v2)
distance_v2 += distance[v1]
distance_v1 += distance[n]

minDistance = min(distance_v1,distance_v2)

if minDistance >= INF:
    print(-1)
else:
    print(minDistance)


# Nth

import heapq

import sys
input = sys.stdin.readline

# 노드 개수, 간선 개수
n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    # a번 정점에서 b번 정점까지 거리가 c인 양방향 간선
    a, b, c = map(int,input().split())

    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int,input().split())

INF = int(1e9)


def dijkstra(start):
    h = []
    heapq.heappush(h,(0,start))
    distance[start] = 0

    while h:
        d, now = heapq.heappop(h)
        if d > distance[now]:
            continue
        for dis, node in graph[now]:
            if d + dis < distance[node]:
                distance[node] = d + dis
                heapq.heappush(h,(d+dis,node))


distance = [INF] * (n+1)
dijkstra(1)
distance_v1 = distance[v1]
distance_v2 = distance[v2]

distance = [INF] * (n+1)
dijkstra(v1)
distance_v1 += distance[v2]
distance_v2 += distance[n]

distance = [INF] * (n+1)
dijkstra(v2)
distance_v2 += distance[v1]
distance_v1 += distance[n]

minDistance = min(distance_v1,distance_v2)

if minDistance >= INF:
    print(-1)
else:
    print(minDistance)
    
# 백준 맞았습니다 뜸

