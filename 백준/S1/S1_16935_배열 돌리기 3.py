# 5,6번 연산 코드 추가해야하고 여러번 연산이 되는지만 확인하면 됨.

# 문제
'''
n*m 배열(n,m:짝수), 연산을 r번 적용, 연산 종류 6가지
list[n][m]
1번 
    : 상하 반전 -> 2k번 수행하면 원본과 같다
    for i in range(n):
        for j in range(n-1,-1,-1):
            l[i] = list[j]

2번
    : 좌우 반전 -> 2k번 수행하면 원본과 같다
    for i in range(n):
        for j in range(m):
            for k in range(m-1,-1,-1)
            l[i][j] = list[i][k]

3번
    : 오른쪽으로 90도 회전 -> 4k번 수행하면 원본과 같다
    for i in range(m):
        for j in range(n):
            l[i][j] = list[n-j][i]

4번
    : 왼쪽으로 90도 회전 -> 4k번 수행하면 원본과 같다
    for i in range(m):
        for j in range(n):
            l[i][j] = list[j][m-i]

'''

# 1st
'''
n, m, r = map(int,input().split())

arr = [0] * n

for i in range(n):
    arr[i] = list(map(int,input().split()))

number = list(map(int,input().split()))



for num in number:
    if num == 1:
        l = [0] * n
        for i in range(n):
            for j in range(n-1,-1,-1):
                l[i] = arr[j]
        arr = l
    elif num == 2:
        # l = [[0 for i in range(n)] for _ in range(m)]
        l = [0] * n
        for i in range(n):
            for j in range(m):
                for k in range(m-1,-1,-1):
                    l[i][j] = arr[i][k]
        arr = l
    elif num == 3:
        l = [[0 for i in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[n-j][i]
        arr = l
    elif num == 4:
        l = [[0 for i in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[j][m-i]
        arr = l


print(arr)
'''

# 2nd

'''
n, m, r = map(int,input().split())

arr = [0] * n

for i in range(n):
    arr[i] = list(map(int,input().split()))

number = list(map(int,input().split()))


# l은 list를 연산 후 결과 리스트
for num in number:
    if num == 1:
        # l에 list값 대입시 행만 쓰니까 초기화도 행만 해줘도 됨
        l = [0] * n
        for i in range(n):
            # l의 위에서 i번째 요소 = list의 아래에서 i번째
            # <=> i <- n-1-i (마즈막 인덱스가 n-1이니까)
            # 위 아래는 행과 관련 있음 -> n 이용
            l[i] = arr[n-1-i]
        arr = l
    elif num == 2:
        # l에 list값 대입시 행열 [][]다 쓰기에 초기화도 행열 다해줘야함
        # 2차원 배열 for 이용해서 선언시 안에 있는 1차원 배열 크기가 열의 크기
        # -> 안에 []가 열의 크기 m, 밖에 []가 행의 크기 n
        l = [[0 for i in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # l의 왼쪽에서 j번째 요소 = list의 오른쪽에서 j번째
                # <=> j <- m-1-j (마즈막 인덱스가 m-1이니까)
                # 좌우는 열과 관련 있음 -> m 이용
                l[i][j] = arr[i][m-1-j]
        arr = l
    elif num == 3:
        l = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[n-1-j][i]
        arr = l
    elif num == 4:
        l = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[j][m-1-i]
        arr = l
    elif num == 5:
        #l1 = [[0] * (n/2) for _ in range(m/2)]
        #l2 = [[0] * (n/2) for _ in range(m/2)]
        #l3 = [[0] * (n/2) for _ in range(m/2)]
        #l4 = [[0] * (n/2) for _ in range(m/2)]
        #l1 = arr[0:n//2][0:m//2]
        # arr[0:n//2][0:m//2] 행은 슬라이싱이 되는데 열이 제대로 슬라이싱 되지 않음
        # l1: [[1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 2, 2, 2, 2]]
        l2 = arr[0:n//2][m//2:m]
        l3 = arr[n//2:n][m//2:m]
        l4 = arr[n//2:n][0:m//2]
        arr[0:n//2][0:m//2] = l4
        arr[0:n//2][m//2:m] = l1
        arr[n//2:n][m//2:m] = l2
        arr[n//2:n][0:m//2] = l3
    elif num == 6:
        l1 = arr[0:n//2][0:m//2]
        l2 = arr[0:n//2][m//2:m]
        l3 = arr[n//2:n][m//2:m]
        l4 = arr[n//2:n][0:m//2]
        arr[0:n//2][0:m//2] = l2
        arr[0:n//2][m//2:m] = l3
        arr[n//2:n][m//2:m] = l4
        arr[n//2:n][0:m//2] = l1



for i in arr:
    print(*i)
'''

# 3rd
'''
n, m, r = map(int,input().split())

arr = [0] * n

for i in range(n):
    arr[i] = list(map(int,input().split()))

number = list(map(int,input().split()))


# l은 list를 연산 후 결과 리스트
for num in number:
    if num == 1:
        # l에 list값 대입시 행만 쓰니까 초기화도 행만 해줘도 됨
        l = [0] * n
        for i in range(n):
            # l의 위에서 i번째 요소 = list의 아래에서 i번째
            # <=> i <- n-1-i (마즈막 인덱스가 n-1이니까)
            # 위 아래는 행과 관련 있음 -> n 이용
            l[i] = arr[n-1-i]
        arr = l
    elif num == 2:
        # l에 list값 대입시 행열 [][]다 쓰기에 초기화도 행열 다해줘야함
        # 2차원 배열 for 이용해서 선언시 안에 있는 1차원 배열 크기가 열의 크기
        # -> 안에 []가 열의 크기 m, 밖에 []가 행의 크기 n
        l = [[0 for i in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # l의 왼쪽에서 j번째 요소 = list의 오른쪽에서 j번째
                # <=> j <- m-1-j (마즈막 인덱스가 m-1이니까)
                # 좌우는 열과 관련 있음 -> m 이용
                l[i][j] = arr[i][m-1-j]
        arr = l
    elif num == 3:
        l = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[n-1-j][i]
        arr = l
    elif num == 4:
        l = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[j][m-1-i]
        arr = l
    elif num == 5:
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for i in range(n//2):
            l1.append([arr[i][0:m//2]])
            l2.append([arr[i][m//2:m]])
        for i in range(n//2,n):
            l3.append([arr[i][m//2:m]])
            l4.append([arr[i][0:m//2]])

        for j in range(n//2):
            arr[j] = l4[j].append(l1[j])
            print("append",arr[j]) # None
        for j in range(n//2,n):
            for k in range(n//2):
                # arr[j] = l3[k] + l2[k] # [2, 1, 3, 8] [3, 2, 6, 3]
                arr[j] = l3[k].extend(l2[k])
                print("extend",arr[j])
    elif num == 6:
        l1 = arr[0:n//2][0:m//2]
        l2 = arr[0:n//2][m//2:m]
        l3 = arr[n//2:n][m//2:m]
        l4 = arr[n//2:n][0:m//2]
        arr[0:n//2][0:m//2] = l2
        arr[0:n//2][m//2:m] = l3
        arr[n//2:n][m//2:m] = l4
        arr[n//2:n][0:m//2] = l1



for i in arr:
    print(*i)
'''

# 4th


n, m, r = map(int,input().split())

arr = [0] * n

for i in range(n):
    arr[i] = list(map(int,input().split()))

number = list(map(int,input().split()))


# l은 list를 연산 후 결과 리스트
for num in number:
    if num == 1:
        # l에 list값 대입시 행만 쓰니까 초기화도 행만 해줘도 됨
        l = [0] * n
        for i in range(n):
            # l의 위에서 i번째 요소 = list의 아래에서 i번째
            # <=> i <- n-1-i (마즈막 인덱스가 n-1이니까)
            # 위 아래는 행과 관련 있음 -> n 이용
            l[i] = arr[n-1-i]
        arr = l
    elif num == 2:
        # l에 list값 대입시 행열 [][]다 쓰기에 초기화도 행열 다해줘야함
        # 2차원 배열 for 이용해서 선언시 안에 있는 1차원 배열 크기가 열의 크기
        # -> 안에 []가 열의 크기 m, 밖에 []가 행의 크기 n
        l = [[0 for i in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # l의 왼쪽에서 j번째 요소 = list의 오른쪽에서 j번째
                # <=> j <- m-1-j (마즈막 인덱스가 m-1이니까)
                # 좌우는 열과 관련 있음 -> m 이용
                l[i][j] = arr[i][m-1-j]
        arr = l
    elif num == 3:
        l = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[n-1-j][i]
        arr = l
        n,m = m,n
        # 3,4번 연산을 통해 가로 세로 길이가 바뀌었음 -> 이후 연산에서 가로,세로 m,n만큼 for문을 돌릴거임
        # -> n,m값도 변경시켜줘야 함
    elif num == 4:
        l = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l[i][j] = arr[j][m-1-i]
        arr = l
        n,m = m,n
    elif num == 5:
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for i in range(n//2):
            l1.append(arr[i][0:m//2])
            l2.append(arr[i][m//2:m])
        for i in range(n//2,n):
            l3.append(arr[i][m//2:m])
            l4.append(arr[i][0:m//2])

        for j in range(n//2):
            # l4[j].append(l1[j])
            l4[j].extend(l1[j])
        # print("l4",l4) # l4 [[[2, 1, 3, 8], [[3, 2, 6, 3]]], [[1, 3, 2, 8], [[9, 7, 8, 2]]], [[4, 5, 1, 9], [[5, 9, 2, 1]]]]
        for j in range(n//2):
            l3[j].extend(l2[j])
        arr = l4 + l3
    elif num == 6:
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for i in range(n//2):
            l1.append(arr[i][0:m//2])
            l2.append(arr[i][m//2:m])
        for i in range(n//2,n):
            l3.append(arr[i][m//2:m])
            l4.append(arr[i][0:m//2])
        
        for j in range(n//2):
            l2[j].extend(l3[j])
            l1[j].extend(l4[j])
        arr = l2 + l1


for i in arr:
    print(*i)

# 백준 맞았습니다.