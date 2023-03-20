# 문제
'''
피자 반죽 지름 제각각
깊이에 따른 오븐의 지름도 제각각(오븐은 관형태)
피자 반죽은 완성되는 순서대로 오븐에 들어가
예)
오븐 / 완성된 반죽 순서 (3 2 5)
5
6    5 (아래 오븐의 지름이 반죽 지름보다 작기에 통과못함)
4
3    2 (위에 오븐의 지름보다 반죽의 지름이 더 작기에 다 통과하다가 아래 반죽이 있기에 여기서 구워짐)
6    3 (아래 2를 통과하지 못함 -> 2 위의 깊이에서 구워짐)
2
3
'''
# 아이디어
'''
완성된 반죽의 지름 < 오븐의 지름 : 다음 오븐의 지름으로 통과
완성된 반죽의 지름 >= 오븐의 지름 : 해당 오븐의 지름을 통과하지 못하고 그 전의(깊이가 덜 깊은 곳) 지름에 걸림
반죽이 이미 있는 깊이의 오븐엔 새 반죽이 들어올 수 없음 -> (이진탐색) 끝값을 바꿔주는 건가? 아님 (dfs or bfs) 방문처리?

'''
# 1st
'''
# 오븐의 깊이, 반죽의 개수 
d, n = map(int,input().split())

# 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름
oven = list(map(int,input().split()))

# 피자 반죽이 완성되는 순서대로의 지름
complete = list(map(int,input().split()))

answer = 0

def search(c):
    global answer
    global end
    for o in range(end):
        if oven[o] > c:
            continue
        elif oven[o] == c:
            answer = o
            end = o-1
        # 오븐 지름과 반죽 지름이 같아도 통과함 그러므로 이 엘이프에서 걸리면 안 됨
        elif oven[o] < c:
            answer = o-1
            end = o-2

end = d  
for i in complete:
    search(i)

print(answer+1)
'''

# 2nd
'''
# 오븐의 깊이, 반죽의 개수 
d, n = map(int,input().split())

# 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름
oven = list(map(int,input().split()))

# 피자 반죽이 완성되는 순서대로의 지름
complete = list(map(int,input().split()))

answer = 0

def search(c):
    global answer
    global end
    for o in range(end):
        # 완성된 반죽이 오븐의 특정 깊이에서 구워질 때마다 end가 재할당됨
        # ( 반죽이 오븐의 특정 깊이에 매칭되지 않고 통과한다면 end값은 변동 x)
        # end값이 -값이라면 더 이상 반죽이 오븐에 들어갈 수 없음 
        # ( 인덱스가 0인 오븐의 최상단 깊이까지 이미 찼다는 말)
        if end < 0:
            print(0)
            exit()
        if oven[o] >= c:
            if o == end:
                answer = o
                end = o -1
            continue
        elif oven[o] < c:
            answer = o-1
            end = o-2

# 애초에 오븐기 깊이보다 반죽이 더 많다면 오븐기에 다 넣을 수가 없음 
if len(oven) < len(complete):
    print(0)
    exit()

end = d  
for i in complete:
    search(i)

print(answer+1)
'''

#3rd
'''
# 오븐의 깊이, 반죽의 개수 
d, n = map(int,input().split())

# 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름
oven = list(map(int,input().split()))

# 피자 반죽이 완성되는 순서대로의 지름
complete = list(map(int,input().split()))

answer = 0

def search(c):
    global answer
    global end
    for o in range(end):    
        if oven[o] >= c:
            if o == d-1:
                answer = o
                #end = o -1
                # range(end)만큼 o를 돌림
                # range(end)는 0 ~ end-1까지 
                # 그래서 굳이 end를 현재 반죽이 들어간 깊이 -1을 안 하고 end = 반죽이 매칭된 깊이로 해줘도
                # range에 의해 그 전 깊이까지만 오븐 깊이를 for로 돌림
                end = o
                # +) end = o-1했을 시, end = 0일 때 o가 0은 돌아야하는데
                #    range에 의해 range(end)는 0~0으로 인하여 for문이 안 돌아감
                return
        elif oven[o] < c:
            answer = o-1
            #end = o-2
            end = o-1
            return

# 애초에 오븐기 깊이보다 반죽이 더 많다면 오븐기에 다 넣을 수가 없음 
if len(oven) < len(complete):
    print(0)
    exit()

end = d  
for i in range(n):
    search(complete[i])
    # 완성된 반죽이 오븐의 특정 깊이에서 구워질 때마다 end가 재할당됨
    # ( 반죽이 오븐의 특정 깊이에 매칭되지 않고 통과한다면 end값은 변동 x
    #   = 반죽이 특정 깊이에 매칭 될때마다 end값이 변함)
    # end값이 0 이하라면 더 이상 반죽이 오븐에 들어갈 수 없음 
    # ( 위에 search함수에서 해당 반죽이 매칭된 깊이 인덱스 = end
    #   즉 search가 돌고 end=0이란 말은 이미 오븐 인덱스 0에 반죽이 들어갔다는 의미
    #   다음 반죽이 들어갈 자리 x )
    if i != n-1 and end <= 0:
        print(0)
        exit()

print(answer+1)
'''
# 백준 시간 초과 뜸

# 4th (블로그)
# 아이디어
'''
오븐이 깊이마다 지름이 다름
위에 있는 깊이의 지름보다 작은 반죽은 아래 오븐에 도달할 수 없음 = 아래 오븐에 올 수 있는 반죽 크기는 위에 오븐의 지름보다 작은 크기들만 가능
처음부터 오븐 깊이를 아래 있는 크기는 위보다 작도록 바꿔줌
ex)
원래  바꾼 리스트
5      5
6      5 (위에 크기가 5니까 아래는 어차피 지름이 5 이하인 반죽만 통과할 수 있음 -> 아예 바꿔줌)
4      4 ( 이미 현재 크기가 위층의 크기보다 작다면 현재 크기 그대로 유지)
3      3
6      3
2      2
3      2
=> (이전에는 크기가 들쑥날쑥했기에 일부 층은 통과하고 특정 깊이에서 걸려서 못 내려왔었으나)
바꾼 리스트에서 아래 층은 위보다 당연히 작기에 위에서 걸려서 아래 못 내려올 일이 없음
-> 오븐의 맨 밑부터 탐색하면서, 현재 위치의 오븐에 피자가 들어올 수 있으면 다음 피자로 넘어가고,
   현재 위치의 오븐에 피자가 들어올 수 없다면 다음 위치(위쪽)의 오븐으로 넘어간다.

-> 위를 반복해서, 오븐의 맨 위까지 탐색을 했는데, 아직 피자가 남아있다면 0을 출력,
   아니라면 가장 위쪽의 피자 위치 출력 ( 가장 위쪽의 피자 위치는 새로운 피자를 넣을때마다 갱신)
 
'''

# 오븐 깊이, 피자 반죽 개수
d, n = map(int,input().split())

# 오븐 깊이별 지름 ( 최상단부터 시작 )
oven = list(map(int,input().split()))

# 피자 반죽 완성되는 순서대로의 반죽 지름
complete = list(map(int,input().split()))

# 현재 깊이의 오븐이 현재보다 상단 깊이의 오븐보다 지름이 크다면 상단 높이의 지름으로 재할당( 작은 크기로 재할당 )
for i in range(1,d):
    oven[i] = min(oven[i],oven[i-1])


answer = 0
start = d-1

# 반죽이 자기보다 큰 지름의 오븐을 만날 때까지 오븐과 비교할 거임
# = 반죽은 조건을 만족하는 오븐을 만나지 못한다면 오븐의 모든 깊이의 지름과 비교할 수 있음
# = 반죽(고정) 오븐(for) -> 반죽이 바깥 for문 + 반죽 for문 안에 오븐 for문
# ( 만약, 오븐이 바깥 for문이면 한 오븐당 모든 반죽이 for문을 돌며 비교되고 조건을 만족하면 체킹됨
#   근데 반죽은 만들어진 순으로 돌아야함)
for c in complete:
    # 오븐의 최하단부터 상단으로 체킹
    if start == -1:
        # 정답일 때 answer에다 +1을 해줄거기 때문에
        # 오븐에 구울 수 없는 경우는 answer을 -1로 두어 0이 출력될 수 있도록 함
        answer = -1
    for i in range(start,-1,-1):
        # 반죽이 오븐보다 작으면 해당 깊이에 반죽 넣기
        if c <= oven[i]:
            answer = i
            # 현재 반죽이 i번째 오븐에 구워졌으면
            # 다음 반죽은 i-1번째 오븐부터 비교되어 조건이 성립한 깊이에서 구워질 수 있음
            start = i-1
            # 반죽이 특정 오븐의 깊이에 매칭 됐으면 다음 오븐과의 비교가 아니라
            # 다음 반죽으로 넘어가야함
            # 현재 for문을 break해서 나가면 아래는 코드가 없으니 다음 반죽으로 넘어가게 됨
            break
        # 반죽이 오븐 지름보다 크면 해당 오븐에 넣을 수 없음 -> 상단 오븐에 재시도
        # 따로 else를 하지 않아도 if문에 걸리지 않으면 for문에 의해 다음 오븐으로 넘어감
        # 해당 반죽이 남아있는 모든 오븐의 지름보다 커서(i가 0일때까지 위의 if문에 걸리지 않은 경우) 들어갈 수 있는 깊이가 없음
        else:
            if i == 0:
                answer = -1
        
# 현재 answer은 oven의 인덱스값이고 인덱스는 0부터 시작하니까 +1
print(answer+1)


