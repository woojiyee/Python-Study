# Q. 한번에 테스트 케이스 정보를 다 받으니까 다 저장하고 있어야 하나? 다 입력 받고 그 다음 함수 등을 돌리나?
# Q. 이전에 어떤 문제는 입력 받는 걸 다 저장 안 하고도 처리를 하고 마저 입력 받고 이랬던 문제가 있었던 거 같은데 차이가 머지?
# 1st
'''
# 테스트 케이스 수
t = int(input("테스트 케이스 수:"))
# 테스트 케이스마다 배추밭 가로
# x[1] = 1번째 테스트 케이스의 배추밭 가로 길이
x = [0] *(t+1)
# 테스트 케이스마다 배추밭 세로
y = [0] *(t+1)
# 테스트 케이스마다 배추 개수
cnt = [0] *(t+1)
# 테스트 케이스마다 배추 그룹 개수 리스트
answer = [0] *(t+1)


# 상하좌우
dy = [1,-1,0,0] # y축이 위아래 -> 배열에선 행
dx = [0,0,1,-1] # x축이 좌우 -> 배열에선 열

#테스트 케이스 : 배추밭 가로,세로 길이, 배추 개수 = 1 : 1
for i in range(1,t+1):
    # 배추밭의 가로 길이, 세로 길이, 배추 개수
    w, h, c = map(int, input("배추밭의 가로 길이, 세로 길이, 배추 개수 입력( 띄워쓰기로 구분 ):").split())
    x[i] = w
    y[i] = h
    cnt[i] = c
    # 테스트 케이스마다 배추 좌표 세트
    # location[1][0][0] = 1번째 테스트 케이스의 지도에서 위치가 (0,0) 곳의 배추 여부
    location = [[[0] * w for _ in range(h)] for _ in range(t+1)]
    for _ in range(c):
        # 배추 x,y 위치
        xy = input("배추의 x, y 좌표:").split()
        # 배추가 있는 좌표를 지도에서 1로 바꿈
        # 가로 길이 x가 열, 세로 길이 y가 행 : xy[0]: location의 열, xy[1] : location의 행 -> location[행][열]
        # print(" location[",i,"][",int(xy[1]),"][",int(xy[0]),"]", location[i][int(xy[1])][int(xy[0])])
        location[i][int(xy[1])][int(xy[0])] = 1

print("배추 위치 리스트 : ",location)

# location에서 인접 배추 세트 갯수 세는 함수
def dfs(location,y,x):
    if location[y][x] == 1:
        location[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            dfs(location,ny,nx)
            return True

# 테스트 케이스별
for i in range(1,t+1):
    # 배추밭 좌표는 0,0부터 시작하니까
    # 테스트 케이스마다 배추 그룹 개수가 있으니 테스트 케이스 바뀔 때마다 리셋
    group = 0
    for w in range(x[i]):
        for h in range(y[i]):
            if dfs(location,h,w) == True:
                group += 1
    answer[i] = group
'''

#2nd


# 테스트 케이스 수
t = int(input())
# 테스트 케이스마다 배추밭 가로
# width[1] = 1번째 테스트 케이스의 배추밭 가로 길이
width = [0] *(t+1)
# 테스트 케이스마다 배추밭 세로
height = [0] *(t+1)
# 테스트 케이스마다 배추 개수
cnt = [0] *(t+1)
# 테스트 케이스마다 배추 그룹 개수 리스트
answer = [0] *(t+1)


# 상하좌우
dy = [1,-1,0,0] # y축이 위아래 -> 배열에선 행
dx = [0,0,1,-1] # x축이 좌우 -> 배열에선 열

#테스트 케이스 : 배추밭 가로,세로 길이, 배추 개수 = 1 : 1
for i in range(1,t+1):
    # 배추밭의 가로 길이, 세로 길이, 배추 개수
    w, h, c = map(int, input().split())
    width[i] = w
    height[i] = h
    cnt[i] = c
    # 테스트 케이스마다 배추 좌표 세트
    # location[1][0][0] = 1번째 테스트 케이스의 지도에서 위치가 (0,0) 곳의 배추 여부
    location = [[[0] * w for _ in range(h)] for _ in range(t+1)]
    for j in range(c):
        #print(j,"번째")
        # 배추 x,y 위치
        xy = input().split()
        #print("xy:",xy)
        # 배추가 있는 좌표를 지도에서 1로 바꿈
        # 가로 길이 x가 열, 세로 길이 y가 행 : xy[0]: location의 열, xy[1] : location의 행 -> location[행][열]
        print(" location[",i,"][",int(xy[1]),"][",int(xy[0]),"]", location[i][int(xy[1])][int(xy[0])])
        location[i][int(xy[1])][int(xy[0])] = 1
        print("후! location[",i,"][",int(xy[1]),"][",int(xy[0]),"]", location[i][int(xy[1])][int(xy[0])])

print("location : ",location)
# location에서 인접 배추 세트 갯수 세는 함수
def dfs(i,location,y,x):
    if x < 0 or x >= width[i] or y < 0 or y >= height[i]:
        return False
    elif location[i][y][x] == 1:
        location[i][y][x] = 0
        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]
            print("j야 돌아라",j)
            print(j,"일 때 dy[j],dx[j]",dy[j],",",dx[j])
            dfs(j,location,ny,nx)
            return True

'''# 테스트 케이스별
for i in range(1,t+1):
    # 배추밭 좌표는 0,0부터 시작하니까
    # 테스트 케이스마다 배추 그룹 개수가 있으니 테스트 케이스 바뀔 때마다 리셋
    group = 0
    for x in range(width[i]):
        for y in range(height[i]):
            if dfs(i,location,y,x) == True:
                group += 1
                print("group+1:",group)
    answer[i] = group
    print("answer[",i,"] : ",answer[i])'''

# 테스트 케이스별
for i in range(1,t+1):
    # 배추밭 좌표는 0,0부터 시작하니까
    # 테스트 케이스마다 배추 그룹 개수가 있으니 테스트 케이스 바뀔 때마다 리셋
    group = 0
    for x in range(width[i]):
        for y in range(height[i]):
            if dfs(i,location,y,x) == True:
                group += 1
                print("group+1:",group)
    answer[i] = group
    print("answer[",i,"] : ",answer[i])

for i in range(1,t+1):
    print(answer[i])
