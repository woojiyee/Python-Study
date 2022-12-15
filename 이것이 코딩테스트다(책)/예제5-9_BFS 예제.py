from collections import deque

# BFS
def bfs(graph, start, visited): 
    # 큐(Oueue) 구현을 위해 deaue 라이브러리 사용 
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 아래서 popleft되고 append되면서 queue가 바뀜
        # -> while문 마즈막 코드인 for문이 다 들아가면
        # 그 바뀐 queue로 다시 while문이 돌아가는 알고리즘
        # 그래서 아래 게속 popleft되는데 인접 노드들이 다 방문처리되서 더 이상 append가 안 되면
        # poplef만 계속 진행되어 queue에는 암것도 안 남게 됨 -> while문 정지
        print("while문 돌아갈 때마다 queue:",queue)
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print( v , end=' ' )
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 
        for i in graph[v]:
            if not visited[i]: 
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
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

# 각 노드의 방문 여부를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
