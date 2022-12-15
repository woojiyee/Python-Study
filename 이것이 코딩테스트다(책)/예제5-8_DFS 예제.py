# DFS 메서드 정의
def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print("방문 처리 된 노드:",v)
    print(v, end = ' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        print("for문 도는 i( 현재 노드의 인접 노드:",i)
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현( 2차원 리스트 )
# graph[n] = [m1,m2,..] : 노드 n의 인접 노드 번호 리스트
# 노드 1번을 graph 리스트 인덱스 1에 넣기 위해 0행에는 빈 리스트 대입
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
] 

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 ( 1차원 리스트 )
# 노드가 9개
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)