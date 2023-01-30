# BFS

#1st
'''from collections import deque

# 수빈, 동생 현재 위치
n, m = map(int,input("수빈이와 동생 위치:").split())

print("수빈이와 동생 위치:",n,m)

graph = [0] * 100000


queue = deque()
queue.append(n)
# graph의 요소는 방문 체킹용이자 시간
# 시작점은 들렸단 의미로 1 대입
graph[n] = 1

print("수빈이 추가한 큐:",queue)

while queue:
    x = queue.popleft()
    print("pop한 큐:",queue)

    for i in [x-1,x+1,x*2]:
        print("i:",i)
        if 0 <= i < 100000:
            if i == m:
                print(graph[i])
                break
            # 방문한 적 있는 위치면 재방문 하지 않고 다음 for문의 요소 돔
            # 이미 방문한 적 있단 말은 시간이 더 적게 걸리고 이곳에 도착했던 다른 루트가 있단 거니까 재방문한 현재 루트는 더 오래 걸리는 루트 -> 답이 될 수 없음
            # 위치 1,3,5,2 루트 , 3,7,4,1,2 루트 중 일단 같은 2를 방문하면 2에서부터 뒤에 루트는 같은 경우의 수들일 거임
            # 그럼 2까지 오는 루트 중 문제는 시간이 적게 고르는 것을 원하니 2까지 오는데 짧게 걸린 루트가 체택 -> 이미 방문했던 적 있는 위치를 방문한 루트는 오래 걸리는 루트 -> 필요 없음
            if graph[i] != 0:
                continue
            queue.append(i)
            graph[i] = graph[x] + 1
            print("i:",i)
            print("time:",graph[i])
            print("append한 큐:",queue)
'''

#2ND

from collections import deque

# 수빈, 동생 현재 위치
n, m = map(int,input("수빈이와 동생 위치:").split())

#if n == m:
#    print("0")
# 여따 적으니 작은 숫자는 잘 되는데 100000 100000 넣으니까 bfs 돌아감
# 왜지? 인터프리터 언어라 위에거 다 돌아야 아래 코드 도는 거 아닌가?

graph = [0] * 100001




def bfs(x):
    queue = deque()
    queue.append(x)
    # graph의 요소는 방문 체킹용이자 시간 구하는 용
    # 시작점은 들렸단 의미로 1 대입
    # 근데 시작점은 시간은 1초 지난게 아니니까 결국 수빈이가 동생한테 가는 루트 걸리는 시간 +1 된 셈 -> 나중에 -1 해주기
    graph[x] = 1

    while queue:
        x = queue.popleft()
        print("pop한 큐:",queue)

        for i in [x-1,x+1,x*2]:
            print("i:",i)
            if 0 <= i <= 100000:
                
                # 방문한 적 있는 위치면 재방문 하지 않고 다음 for문의 요소 돔
                # 이미 방문한 적 있단 말은 시간이 더 적게 걸리고 이곳에 도착했던 다른 루트가 있단 거니까 재방문한 현재 루트는 더 오래 걸리는 루트 -> 답이 될 수 없음
                # 위치 1,3,5,2 루트 , 3,7,4,1,2 루트 중 일단 같은 2를 방문하면 2에서부터 뒤에 루트는 같은 경우의 수들일 거임
                # 그럼 2까지 오는 루트 중 문제는 시간이 적게 고르는 것을 원하니 2까지 오는데 짧게 걸린 루트가 체택 -> 이미 방문했던 적 있는 위치를 방문한 루트는 오래 걸리는 루트 -> 필요 없음
                if graph[i] != 0:
                    continue
                queue.append(i)
                graph[i] = graph[x] + 1
                if i == m:
                    return graph[i]-1
                print("time:",graph[i])
                print("append한 큐:",queue)
if n == m:
    print("0")
else:
    print(bfs(n))