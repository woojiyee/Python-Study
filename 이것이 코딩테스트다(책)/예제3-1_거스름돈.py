#p87
'''문제
거스름돈으로 500원, 100원, 50원, 10원짜리 동전이 무한히 존재
손님에게 거슬러 줘야할 돈이 N원일 때 거슬러 줘야할 동전의 최소 개수는?
단, 거슬러 줘야 할 돈 N은 항상 10의 배수'''

# 수도 코드
'''
* 가장 큰 동전부터 최대 개수 구하기
1. 500 최대 몇개?
2. 100원 > 50원 > 10원 최대 개수'''


# 거슬러 줘야할 돈
N = int(input("거슬러줘야할 돈:"))

# 1st
'''# 동전 수
coin = 0

coin += N // 500

coin += ( N % 500 ) // 100

coin += ( N % 100 ) // 50

coin += ( N % 50 ) // 10'''

# 2nd : 내 코드 + 교재 풀이
# 동전 종류
coin = [500, 100, 50, 10]

# 동전 수
count = 0

for c in coin:
    count += N // c
    N %= c




print(" 거스름돈 동전의 최소 개수:", count)

