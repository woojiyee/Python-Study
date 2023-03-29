# 1st
'''
# 학생 수, 키 비교 횟수
n, m = map(int,input().split())


graph = [[[],[]] for i in range(n+1)]

for i in range(m):
    # 키: a < b
    a, b = map(int,input().split())
    graph[a][1].append(b)
    graph[b][0].append(a)


for i in range(1,n+1):
    # graph[i][0] : 현재 i번째 학생보다 작은 학생들 모음
    for j in graph[i][0]:
        graph[i][0].extend(graph[j][0])

cnt = 0

for i in range(1,n+1):
    if len(graph[i][0]) + len(graph[i][1]) == n-1:
        cnt += 1

print(cnt)
'''
# 백준 메모리 초과 뜸

# 2nd
'''
# 학생 수, 키 비교 횟수
n, m = map(int,input().split())


graph = [[] for i in range(n+1)]

for i in range(m):
    # 키: a < b
    a, b = map(int,input().split())
    graph[b].append(a)


for i in range(1,n+1):
    # graph[i][0] : 현재 i번째 학생보다 작은 학생들 모음
    for j in graph[i]:
        graph[i].extend(graph[j])

cnt = 0

for i in range(1,n+1):
    if len(graph[i]) == n-1:
        cnt += 1

print(cnt)
'''

# 3rd

# 학생 수, 키 비교 횟수
n, m = map(int,input().split())


graph = [[[],[]] for i in range(n+1)]

for i in range(m):
    # 키: a < b
    a, b = map(int,input().split())
    graph[a][1].append(b)
    graph[b][0].append(a)


for i in range(1,n+1):
    # graph[i][0] : 현재 i번째 학생보다 작은 학생들 모음
    for j in graph[i][0]:
        for k in graph[j][0]:
            if k in graph[i][0]:
                continue
            else:
                graph[i][0].append(k)
        

cnt = 0

for i in range(1,n+1):
    if len(graph[i][0]) + len(graph[i][1]) == n-1:
        cnt += 1

print(cnt)