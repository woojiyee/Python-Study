# 문제
'''
- 원래 프린터는 인쇄 명령을 받은 순서대로 인쇄 -> 큐 형식(FIFO)
- 상근이가 프린터기 내부 소프트웨어 개발하여 하단의 조건에 따라 인쇄
1. 현재 큐의 가장 앞에 있는 문서의 '중요도'를 확인
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
   이 문서를 인쇄하지 않고 큐의 가장 뒤에 배치,
   그렇지 않다면 바로 인쇄
-> 일반적인 큐와 같이 앞에서부터 돌면서 현재 문서보다 중요도가 높은 문서가 뒤에 있을 땐 큐의 가장 뒤에 배치,
                               현재 문서가 가장 높은 중요도이면 그대로 출력

ex)
문서 a b c d
중요도 2 1 4 3
-> c d a b

a b c d
1 2 4 3
-> c d b a

=> 결국 명령순이랑 상관 없이 중요도 순으로 출력하게 되는 것 아닌가?
'''

# 1st
'''
# 테스트 케이스 수
t = int(input())

for i in range(t):
    # 문서의 개수 n, 출력순서를 구해야하는 문서의 현재 위치(0부터 시작)
    n, m = map(int,input().split())
    # 문서순서대로 중요도
    for j in range(n):
        list = list(map(int,input().split()))
    number = list[m]
    list.sort(reverse = -1)
    print(list.index(number))
'''   
# 백준 런타임 에러(TypeError) 뜸
# 변수명 list를 arr로 바꾸면 런타임 에러는 안 뜸 함수명이랑 변수명이랑 같게 해서 에러뜬듯?
# 위 코드에서 list 변수명만 arr로 바꾸면 백준 틀렸습니다 뜸 

# 2nd
'''
# 테스트 케이스 수
t = int(input())

for i in range(t):
    # 문서의 개수 n, 출력순서를 구해야하는 문서의 현재 위치(0부터 시작)
    n, m = map(int,input().split())
    # 문서순서대로 중요도
    arr = list(map(int,input().split()))
    for j in range(n):
        arr[j].append(j)

    #target = arr[m]
    arr.sort(reverse = -1)
    #print(arr.index(target))
    for k in range(n):
        for data,index in arr[k]:
            if index == m:
                print(k)
'''
# 백준 	런타임 에러 (AttributeError) 뜸
# arr 입력받은 다음 for문에서
# arr[j]는 리스트가 아니라 정수임, 근데 정수.append는 불가능
# append는 리스트.append와 같이 리스트에만 쓸 수 있는 함수

# 3rd
'''
# 테스트 케이스 수
t = int(input())

for i in range(t):
    # 문서의 개수 n, 출력순서를 구해야하는 문서의 현재 위치(0부터 시작)
    n, m = map(int,input().split())
    # 문서순서대로 중요도
    arr = list(map(int,input().split()))
    for j in range(n):
        arr[j] = [arr[j]]+[j]
    print(arr)

    #target = arr[m]
    arr.sort(reverse = -1)
    #print(arr.index(target))
    for k in range(n):
        if arr[k][1] == m:
            print(k)
'''
# 백준 문제 예시 
# 6 0 / [1,0] [1,1] [9,2] [1,3] [1,4] [1,5] 일 때,
# 연순 정렬하면 [9,2] [1,5] [1,4] [1,3] [1,1] [1,0]으로 정렬됨..
# 9 뒤에 있는 1들은 재정렬되면 안 되는데 sort로 해버리면 모든 1들이 재정렬되버림
# sort를 쓰면 안 됨.. -> 직접 재졍렬해야할 듯 -> 맨 앞 요소를 때야함 -> 큐 사용해야함

# 4th
'''
from collections import deque

# 테스트 케이스 수
t = int(input())

for i in range(t):
    # 문서의 개수 n, 출력순서를 구해야하는 문서의 현재 위치(0부터 시작)
    n, m = map(int,input().split())
    # 문서순서대로 중요도
    q = deque(map(int,input().split()))

    for j in range(n):
        check = q.popleft()
        if len(q) == 0:
            print(j+1)

        # 현재 요소가 가장 큰 요소일 떄
        elif check == max(q):
            if j == m:
                print(j+1)
                break
        else:
            q.append(check)
            # for문은 n회까지만 도는데 뒤에 붙여줌으로써 입력받은 숫자들의 갯수보다 for문을 더 돌려야함..
'''
# 백준 틀렸습니다.

# 5th


from collections import deque

# 테스트 케이스 수
t = int(input())

for i in range(t):
    # 문서의 개수 n, 출력순서를 구해야하는 문서의 현재 위치(0부터 시작)
    n, m = map(int,input().split())
    # 문서순서대로 중요도
    q = deque(map(int,input().split()))
    for j in range(n):
        q[j] = [q[j]]+[j]

    cnt = 1
    while q:
        check = q.popleft()
        if len(q) == 0:
            print(cnt)
        # 현재 요소가 최대값인 요소일 떄, 출력
        # 현재 q가 2차원이라 그냥 max(q)하면 [i,j]이런식으로 나옴
        # 그래서 check >= max(q) 이렇게 하면 인덱스값도 check가 더 커야함
        # 근데 인덱스는 상관 없고 문서의 중요도만 최댓값이면 되기에 [0]해줌
        elif check[0] >= max(q)[0]:
            if check[1] == m:
                print(cnt)
                break
            cnt += 1
            
        else:
            q.append(check)
