# 문제
'''
- 예산의 총액은 정해져있다
- 모든 예상요청대로 배정 못 할 수 있다
- 정해진 총액 이하에서 가능한 최대의 예산을 배정한다
1. 모든 요청이 배정될 수 있는 경우에는 요청 금액 그대로를 배정
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모든 상한액을 배정한다.
   상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정
예)
예산: 485 , 각 요청 : 120, 110, 140, 150
-> 상한액:127        120, 110, 127, 127을 배정하고
그 합이 484로 가능한 최대가 된다'''

# 아이디어
'''
예산을 최대한으로 준다했으니 
총예산을 지방 수로 나눈 평균값 이상으로 줄거임
근데 만약 모든 지방 예산 요청액이 평균값보다 작다면 평균값을 주지 않고 요청대로 줄거임
-> 지방 중 최대 요청 예산금 < (예산 총액 // 지방 수)
   -> 굳이 이진탐색 안 돌리고 최대 요청 금 자체가 배정된 예산 중 최대값
'''

# 1st

# 지방 수
n = int(input())

# 요청 예산액
money = list(map(int,input().split()))

# 총 예산
m = int(input())

def binary(start,end):
    #global temp
    temp = 0
    mid = ( start + end )//2
    if start > end:
        return end
    for i in money:
        if i <= mid:
            temp += i
        else:
            temp += mid
    # 현재 mid가 상한액일 때 지방들 배정 총액
    if temp <= m:
        return binary(mid+1,end)
    if temp > m:
        return binary(start,mid-1)


if sum(money) <= m:
    print(max(money))
else:
    #temp = 0
    print(binary(m//n,max(money)))