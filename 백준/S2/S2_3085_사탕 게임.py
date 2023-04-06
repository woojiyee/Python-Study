#아이디어
'''
인접한 다른 색을 우 또는 하의 색과 교환
교환 이후 같은 색으로 이어진 보드 칸 수 체크
'''
# 1st
'''
n = int(input())

board = [0] * n

for i in range(n):
    list = list(map(int,input().split()))
    for i in range(n-1):
        if list[i] == list[i+1]:
            check = True
            print(n)
            exit()
        else:
            check = False
    board[i] = list


count = 0 

for i in range(n):
    for j in range(n):
        # 오른쪽 색과 다르다면 교환
        if board[i][j] != board[i][j+1]:
            extra = board
            extra[i][j] = board[i][j+1]
            extra[i][j+1] = board[i][j]
            # 좌우 교환시 
            # 행에서 이어진 색깔 수 체크
            cnt = 0
            for k in range(j,0,-1):
                if extra[i][k] == extra[i][k-1]:
                    cnt += 1
                    count = max(cnt, count)
                else:
                    break
            # 열에서 이어진 색깔 수 체크
            cnt = 0
'''
# 모르겠음 ㅠ

# 2nd (블로그)
# https://ji-gwang.tistory.com/245
#아이디어
'''
브루트포스로 다 돌린다. n이 최대 50이므로 가능
한 위치에서 상하좌우와 바꿀 수 있지만 겹치므로 아래와 오른쪽만 계속해서 바꿔준다.
바꿔준 뒤, 전체 보드에서 먹을 수 있는 사탕의 최대 개수를 구한 뒤 원상 복구 해주고
다음 걸로 넘어가 바꿔주고 확인하고를 반복하면 된다.

시간복잡도 : O(n^4) : 50 ** 4 = 6250000 < 2억 -> 가능 
'''
n = int(input())

array = []
for _ in range(n):
    colors = list(map(str, input()))
    array.append(colors)

maxCount = 0 #최대 사탕 개수를 초기화

# 배열의 행 마다 같은 색의 사탕이 몇개 연이어 있는지 계산
def width():
    global  maxCount
    
    for k in range(n):
        countRow = 1 #초기 개수를 1로 초기화
        for l in range(n - 1):
            if array[k][l] == array[k][l + 1]: #만약 해당 사탕과 오른쪽 사탕의 색이 같다면 / 행 ==. 열 !=
                countRow += 1 #사탕 개수 1 증가
                maxCount = max(maxCount,countRow) #증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else: #만약 좌우 사탕 색 다르다면
                countRow = 1 #개수를 1로 초기화 / 이어지던 색이 끊기고 새로 셀거니까


# 배열의 열마다 같은 색의 사탕이 몇개 연이어 있는지 계산
def height():
    for k in range(n):
        global maxCount
        
        countColumn = 1 #초기 개수를 1로 초기화
        for l in range(n - 1):
            if array[l][k] == array[l + 1][k]: #만약 해당 사탕과 아래쪽 사탕의 색이 같다면 / 행 !=. 열 ==
                countColumn += 1 #사탕 개수를 1개씩 증가시켜주고
                maxCount = max(maxCount,countColumn) #증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else: #만약 상하 사탕 색이 다르다면
                countColumn = 1 #개수를 1로 초기화


for i in range(n):
    for j in range(n - 1):
        # 만약 입력 받은 배열의 행의 원소가 다르다면 
        if array[i][j] != array[i][j + 1]:
            # 행 고정 열 교환 후 연이은 같은 색 최대 사탕 수 구하기
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            width()
            height()
            # 다음 경우의 수를 구하기 위해 원래 사탕 배치로 원상 복구
            array[i][j + 1], array[i][j] = array[i][j], array[i][j + 1]
        # 만약 입력 받은 배열의 열의 원소가 다르다면 
        if array[j][i] != array[j + 1][i]:
            # 열 고정 행 교환 후 연이은 같은 색 최대 사탕 수 구하기
            array[j][i], array[j + 1][i] = array[j + 1][i], array[j][i]
            width()
            height()
            array[j + 1][i], array[j][i] = array[j][i], array[j + 1][i]

print(maxCount) #색이 같은 사탕개수 최대값을 출력

# 백준 맞았습니다.





