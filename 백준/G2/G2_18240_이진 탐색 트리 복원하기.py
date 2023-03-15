# 해결못함 
# 1st
'''
# 수열 길이(노드 수)
n = int(input())

# 입력받은 노드들의 간선( 깊이 /level )
level = []

# 1.
# 루트노드는 입력받지 않으니까 노드 수-1만큼 입력받음
for i in range(n-1):
    level.append(map(int,input().split())) # map형식 이래 뜸 (level에 제대로 안 들어감 )

# 2.
level.append(map(int,input().split())) # level[0]에 [1,2,1,2]로 들어감

# ->
level = list(map(int,input().split())) # 이렇게 해야 level = [1,2,1,2]로 들어감



nodeCnt = [0] * (n+1)
nodeCnt[0] = 1
sub = [0] *(n+1)
sub[0] = 1
sub[1] = 2
for j in level:
    # 부모 노드가 없다면
    # 자식 노드가 먼저 입력됬을 때
    # 부모 노드 없이 자식 노드부터 이진 탐색 트리가 구현될 수 없음
    if nodeCnt[j-1] <= 0:
        print(-1)
        exit()
    nodeCnt[j] += 1
    sub[j+1] += 2
    # 각 레벨당 입력받은 부모 노드로 만들 수 있는 자식 노드 수보다 입력 받은 노드 수가 많으면 이진 탐색 트리 불가능
    if nodeCnt[j] > sub[j]:
        print(-1)
        exit()

print("가능")
'''

'''# 2nd

# 수열 길이(노드 수)
n = int(input())

# 입력받은 노드들의 간선( 깊이 /level )
#level = [map(int,input().split())]
level = list(map(int,input().split()))

nodeCnt = [0] * (n+1)
nodeCnt[0] = 1
sub = [0] *(n+1)
sub[0] = 1
sub[1] = 2
for j in level:
    # 부모 노드가 없다면
    # 자식 노드가 먼저 입력됬을 때
    # 부모 노드 없이 자식 노드부터 이진 탐색 트리가 구현될 수 없음
    if nodeCnt[j-1] <= 0:
        print(-1)
        exit()
    nodeCnt[j] += 1
    if j <= n:
        sub[j+1] += 2
    # 각 레벨당 입력받은 부모 노드로 만들 수 있는 자식 노드 수보다 입력 받은 노드 수가 많으면 이진 탐색 트리 불가능
    if nodeCnt[j] > sub[j]:
        print(-1)
        exit()

print("가능")
'''

# 2nd
'''
from collections import deque

# 수열 길이(노드 수)
n = int(input())

# 입력받은 노드들의 간선( 깊이 /level )
#level = [map(int,input().split())]
level = list(map(int,input().split()))

nodeCnt = [0] * (n+1)
nodeCnt[0] = 1
sub = [0] *(n+1)
sub[0] = 1
sub[1] = 2
for j in level:
    # 부모 노드가 없다면
    # 자식 노드가 먼저 입력됬을 때
    # 부모 노드 없이 자식 노드부터 이진 탐색 트리가 구현될 수 없음
    if nodeCnt[j-1] <= 0:
        print(-1)
        exit()
    nodeCnt[j] += 1
    if j <= n:
        sub[j+1] += 2
    # 각 레벨당 입력받은 부모 노드로 만들 수 있는 자식 노드 수보다 입력 받은 노드 수가 많으면 이진 탐색 트리 불가능
    if nodeCnt[j] > sub[j]:
        print(-1)
        exit()

print("가능")'''

# 3rd
'''
from collections import deque

# 수열 길이(노드 수)
n = int(input())

# 입력받은 노드들의 간선( 깊이 /level )
#level = [map(int,input().split())]
level = list(map(int,input().split()))

nodeCnt = [0] * (n+1)
nodeCnt[0] = 1
sub = [0] *(n+1)
sub[0] = 1
sub[1] = 2
for j in level:
    # 부모 노드가 없다면
    # 자식 노드가 먼저 입력됬을 때
    # 부모 노드 없이 자식 노드부터 이진 탐색 트리가 구현될 수 없음
    if nodeCnt[j-1] <= 0:
        print(-1)
        exit()
    nodeCnt[j] += 1
    if j <= n:
        sub[j+1] += 2
    # 각 레벨당 입력받은 부모 노드로 만들 수 있는 자식 노드 수보다 입력 받은 노드 수가 많으면 이진 탐색 트리 불가능
    if nodeCnt[j] > sub[j]:
        print(-1)
        exit()

time = 1
q = deque()
q.append([time,0])
# q ([time,0],[time,1])
print("q",q)

def make():
    # q = deque([time,0])
    for i in level:
        for k in q:
            print("k",k)
            j = k[0]
            # q에 있는 j의 부모 노드
            if i-1 == j:
                index = q.index(j)
                if q[j-1] == i:
                    if q[j+1] == i:
                        continue
                    q.append([time,j])
                time += 1
                q.appendleft([time,j])

make()

for i in range(1,n+1):
    if q[i][0] == i:
        print(i,end = ' ')
'''

# 4th
'''
from collections import deque

# 수열 길이(노드 수)
n = int(input())

# 입력받은 노드들의 간선( 깊이 /level )
#level = [map(int,input().split())]
level = list(map(int,input().split()))

nodeCnt = [0] * (n+1)
nodeCnt[0] = 1
sub = [0] *(n+1)
sub[0] = 1
sub[1] = 2
for j in level:
    # 부모 노드가 없다면
    # 자식 노드가 먼저 입력됬을 때
    # 부모 노드 없이 자식 a노드부터 이진 탐색 트리가 구현될 수 없음
    if nodeCnt[j-1] <= 0:
        print(-1)
        exit()
    nodeCnt[j] += 1
    if j <= n:
        sub[j+1] += 2
    # 각 레벨당 입력받은 부모 노드로 만들 수 있는 자식 노드 수보다 입력 받은 노드 수가 많으면 이진 탐색 트리 불가능
    if nodeCnt[j] > sub[j]:
        print(-1)
        exit()

time = 1
q = deque()
q.append([time,0])

while len(q) <= n:
    for i in level:
        for j in range(len(q)):
            # level에 있는 노드의 부모 노드가 q에 있느가
            if q[j][1] == i-1:
                # 이미 부모 노드 j가 맨 왼쪽의 노드일 때
                if j-1 < 0 :
                    time += 1
                    q.appendleft([time,i])
                    break
                # 부모 노드 왼쪽에 이미 해당 노드 간선값과 같은 노드가 있을 때
                elif q[j-1][1] == i:
                    # 부모의 오른쪽에도 이미 있을 떄
                    if q[j+1][1] == i:
                        continue
                    else:
                        time += 1
                        q.append([time,i])
                        break
                else:
                    time += 1
                    q.appendleft([time,i])
                    break


for i in range(5):
    for j in range(5):
        if q[j][0] == i:
            print(j,end = ' ')
'''

# 5th
'''
from collections import deque

# 수열 길이(노드 수)
n = int(input())

# 입력받은 노드들의 간선( 깊이 /level )
#level = [map(int,input().split())]
level = list(map(int,input().split()))

nodeCnt = [0] * (n+1)
nodeCnt[0] = 1
sub = [0] *(n+1)
sub[0] = 1
sub[1] = 2
for j in level:
    # 부모 노드가 없다면
    # 자식 노드가 먼저 입력됬을 때
    # 부모 노드 없이 자식 a노드부터 이진 탐색 트리가 구현될 수 없음
    if nodeCnt[j-1] <= 0:
        print(-1)
        exit()
    nodeCnt[j] += 1
    if j <= n:
        sub[j+1] += 2
    # 각 레벨당 입력받은 부모 노드로 만들 수 있는 자식 노드 수보다 입력 받은 노드 수가 많으면 이진 탐색 트리 불가능
    if nodeCnt[j] > sub[j]:
        print(-1)
        exit()

time = 1
q = deque()
q.append([time,0])

while len(q) < n:
    for i in level:
        for j in range(len(q)):
            # level에 있는 노드의 부모 노드가 q에 있느가
            if q[j][1] == i-1:
                # 이미 부모 노드 j가 맨 왼쪽의 노드일 때
                if j-1 < 0 :
                    time += 1
                    q.appendleft([time,i])
                    break
                # 부모 노드 왼쪽에 이미 해당 노드 간선값과 같은 노드가 있을 때
                elif q[j-1][1] == i:
                    # 부모의 오른쪽에도 이미 있을 떄
                    if j > len(q):
                        if q[j+1][1] == i:
                            continue
                    else:
                        time += 1
                        q.insert(j+1,[time,i])
                        break
                else:
                    time += 1
                    q.insert(j,[time,i])
                    break


for i in range(1,n+1):
    for j in range(n):
        if q[j][0] == i:
            print(j+1,end = ' ')
'''

# 6th

# 수열 길이(노드 수)
n = int(input())

# 입력받은 노드들의 간선( 깊이 /level )
#level = [map(int,input().split())]
level = list(map(int,input().split()))

nodeCnt = [0] * (n+1)
nodeCnt[0] = 1
sub = [0] *(n+1)
sub[0] = 1
sub[1] = 2
for j in level:
    # 부모 노드가 없다면
    # 자식 노드가 먼저 입력됬을 때
    # 부모 노드 없이 자식 a노드부터 이진 탐색 트리가 구현될 수 없음
    if nodeCnt[j-1] <= 0:
        print(-1)
        exit()
    nodeCnt[j] += 1
    if j <= n:
        sub[j+1] += 2
    # 각 레벨당 입력받은 부모 노드로 만들 수 있는 자식 노드 수보다 입력 받은 노드 수가 많으면 이진 탐색 트리 불가능
    if nodeCnt[j] > sub[j]:
        print(-1)
        exit()

time = 1
list = [[time,0]]

while len(list) < n:
    for i in level:
        for j in range(n):
            if i-1 == list[j][1]:
                if i in list[0:j-1]:




for i in range(1,n+1):
    for j in range(n):
        if list[j][0] == i:
            print(j+1,end = ' ')


