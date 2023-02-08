# DP 다이나믹 프로그래밍

# 문제
'''
조건
인접한 두 집은 색이 같으면 안 된다.
모든 집을 칠하는 비용의 최솟값'''

# 1st

# 집 수
n = int(input())
house = [0] * n
# house = [] * n
# 빈 배열로 하면 아래 house[i]에서 에러 뜸
print(house)

for i in range(n):
    house[i] = list(map(int,input().split()))

print(house)

# 현재 집이 r일 때 전집은 g,b일 수 있음 
# gr,gb의 최소값 비교를 위해
array = list()

print(array)

for i in range(1,n):
    for j in range(3):
        # 현재 집 인덱스(색깔을 의미) j
        before = j
        for k in range(3):
            # 현재 집의 색깔과 같지 않는 전집만 체킹
            if k != before:
                array.append(house[i-1][k]+house[i][j])
        # array 중 최솟값이 현재 house[i][j]까지의 최소 비용
        # 다음 집은 현재집까지의 비용에다 다음 집 비용을 더하는거니까 그냥 house값을 바꿔주기!
        house[i][j] = min(array)
        array = list()

print(min(house[n-1]))
                



