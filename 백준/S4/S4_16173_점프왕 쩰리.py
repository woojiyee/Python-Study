'''
문제 규칙
1. 정사각형 구역 내부에서만 이동 가능
2. 출발점은 항상 가장 왼쪽, 가장 위칸 ( 다른 지점에선 출발 x)
3, 오른쪽 , 아래쪽으로만 이동 가능
4. 쩰리가 가장 오른쪽 , 가장 아래칸에 도달 시 젤리 승 -> 게임 종료
5. 한번에 이동할 수 있는 칸의 수는 현재 밟고 있는 칸에 쓰여 있는 수 만큼 ( 칸에 쓰여있는 수 초과 또는 미만으로 이동 불가 )
쩰리가 게임 구역에서 끝 점( 맨 오른쪽, 맨 아래칸)까지 도달 가능 여부를 알아보자!
'''

# 1st
'''
# 구역 크기
n = int(input("구역 크기 입력:"))

# 구역 지도 리스트
gameMap = [[] for _ in range(n)]

# 마즈막 행에서 이동, 마즈막 열에서 이동이 게임 판 범위를 벗어나는지 체크하는 변수
check = 0

for i in range(n):
    gameMap[i] = list(map(int,input("게임판 입력: ").split())) # 리스트 자료형이 아닌 map 자료형으로 대입됨
    # list.append(list(map(int,input("게임판 입력:").split())))

print("게임판: ", gameMap)

def dfs(y,x,gameMap):
    global check
    # 마지막 열에서도 쩰리가 게임판 범위를 초과했고 행에서도 범위 초괴
    # -> 승리 지점에 도달할 수 없음 -> 실패한 경우
    if check == 2:
        print("Hing")
    if n <= x:
        # 마지막 행인데 x값 초과
        if y == n-1:
            check += 1
    elif n <= y :
        # 마지막 열인데 y값 초과
        if x == n-1:
            check += 1
    else:
        # 이동된 위치가 승리 지점이라면
        if gameMap(y,x) == -1:
            print("HaruHaru")
        # 우측으로 칸에 쓰인 숫자만큼 이동
        dfs(x + gameMap(y,x),y,gameMap)
        # 하측으로 칸에 쓰인 숫자만큼 이동
        dfs(x, y + gameMap(y,x),gameMap)

print("gameMap[1][1]:", gameMap[1][1])
dfs(0,0,gameMap)
'''

# 2nd
'''
# 구역 크기
n = int(input())

# 구역 지도 리스트
gameMap = [[] for _ in range(n)]

# 마즈막 행에서 이동, 마즈막 열에서 이동이 게임 판 범위를 벗어나는지 체크하는 변수
check = 0

for i in range(n):
    gameMap[i] = list(map(int,input().split())) # 리스트 자료형이 아닌 map 자료형으로 대입됨
    # gameMap.append(list(map(int,input().split())))

print("gameMap[1][1]:",gameMap[1][1])
def dfs(y,x,gameMap):
    global check
    # x,y의 최대 인덱스는 n-1이니까 x,y가 n 이상이라면 게임판 범위를 벗어난 경우
    if n <= x:
        # 열을 벗어난 경우 중 (x값 초과) 마즈막 행인 경우
        if y == n-1:
            check += 1
            # 마지막 열에서도 쩰리가 게임판 범위를 초과했고 행에서도 범위 초과 (check가 두번 됐으니)
            # -> 승리 지점에 도달할 수 없음 -> 실패한 경우
            if check == 2:
                print("Hing")
                return 
    elif n <= y :
        # 행을 벗어난 경우 중 (y값 초과) 마즈막 열인 경우
        if x == n-1:
            check += 1
            # 마지막 열에서도 쩰리가 게임판 범위를 초과했고 행에서도 범위 초과 (check가 두번 됐으니)
            # -> 승리 지점에 도달할 수 없음 -> 실패한 경우
            if check == 2:
                print("Hing")
                return 
    else:
        # 이동된 위치가 승리 지점이라면
        if gameMap[y][x] == -1:
            print("HaruHaru")
            return # return 안쓰니까 HaruHaru 여러번 출력 됨
        # 우측으로 칸에 쓰인 숫자만큼 이동
        dfs(y, x + gameMap[y][x],gameMap)
        # 하측으로 칸에 쓰인 숫자만큼 이동
        dfs(y + gameMap[y][x],x,gameMap)
        

dfs(0,0,gameMap)
'''

# 3rd

    
# 구역 크기
n = int(input())

# 구역 지도 리스트
gameMap = [[] for _ in range(n)]

# 마즈막 행에서 이동, 마즈막 열에서 이동이 게임 판 범위를 벗어나는지 체크하는 변수
check = 0

for i in range(n):
    gameMap[i] = list(map(int,input().split())) 

def dfs(y,x):
    global check
    # x,y의 최대 인덱스는 n-1이니까 x,y가 n 이상이라면 게임판 범위를 벗어난 경우
    if n <= x:
        # 열을 벗어난 경우 중 (x값 초과) 마즈막 행인 경우
        if y == n-1:
            check += 1
            # 마지막 열에서도 쩰리가 게임판 범위를 초과했고 행에서도 범위 초과 (check가 두번 됐으니)
            # -> 승리 지점에 도달할 수 없음 -> 실패한 경우
            if check == 2:
                print("Hing")
                return 
    elif n <= y :
        # 행을 벗어난 경우 중 (y값 초과) 마즈막 열인 경우
        if x == n-1:
            check += 1
            # 마지막 열에서도 쩰리가 게임판 범위를 초과했고 행에서도 범위 초과 (check가 두번 됐으니)
            # -> 승리 지점에 도달할 수 없음 -> 실패한 경우
            if check == 2:
                print("Hing")
                return 
    else:
        if gameMap[y][x] == 0:
            check += 1
            if check == 2:
                print("Hing")
        # 이동된 위치가 승리 지점이라면
        if gameMap[y][x] == -1:
            print("HaruHaru")
            return # return 안쓰니까 HaruHaru 여러번 출력 됨
        # 우측으로 칸에 쓰인 숫자만큼 이동
        dfs(y, x + gameMap[y][x])
        # 하측으로 칸에 쓰인 숫자만큼 이동
        dfs(y + gameMap[y][x],x)
        

dfs(0,0)
