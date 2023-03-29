# 알고리즘
'''
1. 입력 받을시, 범위 밖은 저장 x
2. 이득 거리(범위 실 거리 - 지름길 거리)가 음수인 입력값도 저장 x
3. 입력 받을 시 이득 거리도 계산해서 같이 저장
4. 이득 거리 기준으로 내림 차순 정렬
5. 이득 거리가 큰 순으로 체킹(반복문 돌기)
6. 큐 저장 시, 이득 거리는 제외한 원소만 저장
7. if 현재 큐에 있는 원소의 시작값 > 체킹할 원소의 종료값
    leftappend
   elif 현큐 원소 종료값 < 체킹 원소 시작값
    append
   else
    continue
+
start = 0
dis = 0
while q:
    qStart, qEnd, qDis = q.popleft
    dis = qStart - start + qDis
    start = qEnd
'''

# 1st
'''
from collections import deque

n, dis = map(int,input().split())
list = []

for i in range(n):
    s, e, d = map(int,input().split())
    # 지름길의 종료위치가 도로의 길이보다 크다면 범위 초과인 셈
    # 저장 안 하고 다음 입력 받기
    if e > dis:
        continue
    # 실제 거리 보다 지름길 거리가 작으면 저장
    if e - s > d:
        # 실제 거리보다 얼마나 더 짧은지 = 이득 거리라 하겠음
        list.append([(e - s)- d,s,e,d])
    # 실제 거리보다 지름길 거리가 길면 저장하지 않음

# 이득 거리가 큰 순으로 정렬하기 위해 내림차순 정렬
# list의 원소인 리스트에 이득 거리가 제일 처음 원소이기에 이득거리를 기준으로 정렬됨
list.sort(reverse=True)

# list = list[:][1:]

# 입력값을 다 리스트에 저장한 것이 아니기에 리스트 길이를 새로 구함
length = len(list)

# 시작위치
start = 0

# 거리
answer = 0

# 이득 거리가 가장 큰 지름길을 넣어줌
# 이득 거리는 제외한 원소들만 넣어줌
#q = deque(list[0][1:])
q = deque([list[0]])

for i in range(1,length):
    for j in q:
        # 이미 큐에 있는 선택된 지름길의 시작값보다 체킹 중인 지름길의 종료값이 더 작은가?
        if j[1] >= list[i][2]:
            # 체킹 중인 지름길이 더 이전의 위치라는 의미
            q.appendleft(list[i])
            # append하게 되면 큐 원소가 생김 현재 포문이 큐 원소만큼 도는거라 꼬임
            # 그래서 append하고 큐 for문 나가게 break하기
            break
        # 체킹 중인 지름길의 시작값이 선택된 지름길의 종료값보다 크다면
        elif j[2] <= list[i][1]:
            # 체킹 중인 지름길이 더 이후의 위치라는 의미
            q.append(list[i])
            break
        # 위에 있는 경우에 속하지 않는다는 것은 체킹 중인 지름길 위치가 이미 선택된 지름길에 포함되어 있거나 아님 겹치는 구간이 있다는 의미
        else:
            # 다른 선택된 지름길과 비교하지 않아도 되므로 해당 지름길은 해당 for문 종료
            break
 
while q:
    a, qStart, qEnd, qDis = q.popleft()
    # 계속 거리는 추가되어야하므로 재할당 =이 아니라 +=으로!!
    answer += qStart - start + qDis
    start = qEnd

# 큐에 마즈막 원소의 종료값(위치)가 고속도로 전체 종료값(위치)와 다를 수 있으므로 체킹하기
answer += dis - qEnd

print(answer)
'''
# 1st 백준 틀렸습니다
# 1st 코드는 이득 거리가 큰 순으로 체택을 해서 이후에 이미 체택한 루트와 겹치면 선택을 안 하도록 함
# 예를 들어 (시작 위치,종료 위치, 이득 거리) [40,60,5] 근데 [40,50,4],[50,60,4]이러면
# 이득 거리가 5인 애가 우선 순위가 높아서 먼저 체택되어 겹치는 위치인 뒤에 두 지름길은 선택이 안 됨
# 근데 실제론 [40,50,4],[50,60,4] 이 루트가 총 이득 거리 8로 한 지름길을 택한 이득 거리 5보다 큼
# -> 다 선택해가며 비교해야한다는 소린데 bfs처럼 방문 체크하면서 다 돌고 거리가 얼마나 걸렸는지 확인해야하는건가?
# 근데 지름길의 종료 위치가 고속도로의 종료 위치랑 같다는 보장도 없으니 모든 방문값에 종료 위치도 저장해서 고속도로 종료 위치까지의 거리를 더한 값 중에 최솟값을 찾아야하는건가?

# 2nd
'''
from collections import deque

n, dis = map(int,input().split())
list = []

for i in range(n):
    s, e, d = map(int,input().split())
    # 지름길의 종료위치가 도로의 길이보다 크다면 범위 초과인 셈
    # 저장 안 하고 다음 입력 받기
    if e > dis:
        continue
    # 실제 거리 보다 지름길 거리가 작으면 저장
    if e - s > d:
        # 실제 거리보다 얼마나 더 짧은지 = 이득 거리라 하겠음
        list.append([(e - s)- d,s,e,d])
    # 실제 거리보다 지름길 거리가 길면 저장하지 않음

# 이득 거리가 큰 순으로 정렬하기 위해 내림차순 정렬
# list의 원소인 리스트에 이득 거리가 제일 처음 원소이기에 이득거리를 기준으로 정렬됨
list.sort(reverse=True)

# list = list[:][1:]

# 입력값을 다 리스트에 저장한 것이 아니기에 리스트 길이를 새로 구함
length = len(list)

ll = []

for i in range(length):
    # 이득 거리가 가장 큰 지름길을 넣어줌
    # 이득 거리는 제외한 원소들만 넣어줌
    q = deque([list[i]])
    ll.append(q)

def distance(k):
    q = ll[k]
    # 시작위치
    start = 0
    # 거리
    answer = 0
    for i in range(length):
        if i != k:
            for j in q:
                # 이미 큐에 있는 선택된 지름길의 시작값보다 체킹 중인 지름길의 종료값이 더 작은가?
                if j[1] >= list[i][2]:
                    # 체킹 중인 지름길이 더 이전의 위치라는 의미
                    q.appendleft(list[i])
                    # append하게 되면 큐 원소가 생김 현재 포문이 큐 원소만큼 도는거라 꼬임
                    # 그래서 append하고 큐 for문 나가게 break하기
                    break
                # 체킹 중인 지름길의 시작값이 선택된 지름길의 종료값보다 크다면
                elif j[2] <= list[i][1]:
                    # 체킹 중인 지름길이 더 이후의 위치라는 의미
                    q.append(list[i])
                    break
                # 위에 있는 경우에 속하지 않는다는 것은 체킹 중인 지름길 위치가 이미 선택된 지름길에 포함되어 있거나 아님 겹치는 구간이 있다는 의미
                else:
                    # 다른 선택된 지름길과 비교하지 않아도 되므로 해당 지름길은 해당 for문 종료
                    break
    
    while q:
        a, qStart, qEnd, qDis = q.popleft()
        # 계속 거리는 추가되어야하므로 재할당 =이 아니라 +=으로!!
        answer += qStart - start + qDis
        start = qEnd

    # 큐에 마즈막 원소의 종료값(위치)가 고속도로 전체 종료값(위치)와 다를 수 있으므로 체킹하기
    answer += dis - qEnd

    return answer

minDis = 10000

for k in range(length):
    minDis = min(minDis,distance(k))

print(minDis)
'''

# 3TH
'''
from collections import deque

n, dis = map(int,input().split())
list = []

for i in range(n):
    s, e, d = map(int,input().split())
    # 지름길의 종료위치가 도로의 길이보다 크다면 범위 초과인 셈
    # 저장 안 하고 다음 입력 받기
    if e > dis:
        continue
    # 실제 거리 보다 지름길 거리가 작으면 저장
    if e - s > d:
        # 실제 거리보다 얼마나 더 짧은지 = 이득 거리라 하겠음
        list.append([(e - s)- d,s,e,d])
    # 실제 거리보다 지름길 거리가 길면 저장하지 않음

# 이득 거리가 큰 순으로 정렬하기 위해 내림차순 정렬
# list의 원소인 리스트에 이득 거리가 제일 처음 원소이기에 이득거리를 기준으로 정렬됨
list.sort(reverse=True)

# 입력값을 다 리스트에 저장한 것이 아니기에 리스트 길이를 새로 구함
length = len(list)

ll = []

for i in range(length):
    q = deque([list[i]])
    ll.append(q)

def distance(k):
    q = ll[k]
    # 시작위치
    start = 0
    # 총 이동 거리
    answer = 0
    for i in range(length):
        if i != k:
            for j in q:
                # 이미 큐에 있는 선택된 지름길의 시작값보다 체킹 중인 지름길의 종료값이 더 작은가?
                if j[1] >= list[i][2]:
                    # 체킹 중인 지름길이 더 이전의 위치라는 의미
                    extra = q.pop()
                    q.append(list[i])
                    q.append(extra)
                    break
                # 체킹 중인 지름길의 시작값이 선택된 지름길의 종료값보다 크다면
                elif j[2] <= list[i][1]:
                    # 체킹 중인 지름길이 더 이후의 위치라는 의미
                    if len(q) == 1:
                        q.append(list[i])
                        break
                    else:
                        continue
                # 위에 있는 경우에 속하지 않는다는 것은 체킹 중인 지름길 위치가 이미 선택된 지름길에 포함되어 있거나 아님 겹치는 구간이 있다는 의미
                else:
                    # 다른 선택된 지름길과 비교하지 않아도 되므로 해당 지름길은 해당 for문 종료
                    break
    
    while q:
        a, qStart, qEnd, qDis = q.popleft()
        answer += qStart - start + qDis
        start = qEnd

    # 큐에 마즈막 원소의 종료값(위치)가 고속도로 전체 종료값(위치)와 다를 수 있으므로 체킹하기
    answer += dis - qEnd

    return answer

minDis = 10000

for k in range(length):
    minDis = min(minDis,distance(k))

print(minDis)
'''

# 3th 주석 지운 거
'''
from collections import deque

n, dis = map(int,input().split())
list = []

for i in range(n):
    s, e, d = map(int,input().split())
    if e > dis:
        continue
    if e - s > d:
        list.append([(e - s)- d,s,e,d])

list.sort(reverse=True)

length = len(list)

ll = []

for i in range(length):
    q = deque([list[i]])
    ll.append(q)

def distance(k):
    q = ll[k]
    start = 0
    answer = 0
    for i in range(length):
        if i != k:
            for j in q:
                if j[1] >= list[i][2]:
                    extra = q.pop()
                    q.append(list[i])
                    q.append(extra)
                    break
                elif j[2] <= list[i][1]:
                    if len(q) == 1:
                        q.append(list[i])
                        break
                    else:
                        continue
                else:
                    break
    
    while q:
        a, qStart, qEnd, qDis = q.popleft()
        answer += qStart - start + qDis
        start = qEnd

    answer += dis - qEnd

    return answer

minDis = 10000

for k in range(length):
    minDis = min(minDis,distance(k))

print(minDis)'''

# 4th


from collections import deque

n, dis = map(int,input().split())
list = []

for i in range(n):
    s, e, d = map(int,input().split())
    if e > dis:
        continue
    if e - s > d:
        list.append([(e - s)- d,s,e,d])

list.sort(reverse=True)

length = len(list)

ll = []

for i in range(length):
    q = deque([list[i]])
    ll.append(q)

def distance(k):
    q = ll[k]
    start = 0
    benefit = 0
    for i in range(length):
        if i != k:
            for j in q:
                if j[1] >= list[i][2]:
                    extra = q.pop()
                    q.append(list[i])
                    q.append(extra)
                    break
                elif j[2] <= list[i][1]:
                    if len(q) == 1:
                        q.append(list[i])
                        break
                    else:
                        continue
                else:
                    break
    
    while q:
        b, qStart, qEnd, qDis = q.popleft()
        benefit += b
        # 3th처럼 끊기는 거 다 체크 안해도
        # 결국 이득 거리만큼 전체 거리에서 줄어든거니 이득 거리 총합을 구해서
        # 전체 거리서 이득 거리 빼면 지름길을 이용한 루트의 이동 거리인 셈

    answer = dis - benefit

    return answer

minDis = 10000

for k in range(length):
    minDis = min(minDis,distance(k))

print(minDis)