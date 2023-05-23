# 1st
'''
n = int(input())

empty = " "
star = "*"

for i in range(n+1):
    print(empty*(n-i)+star*i)
'''
# 백준 "출력 형식이 잘못되었습니다" 뜸

# 2nd

n = int(input())

empty = " "
star = "*"

for i in range(1,n+1):
    print(empty*(n-i)+star*i)

# 백준 맞았습니다.
# 첨에 * 무조건 한개 찍혀야하니까 for문에 i는 1부터 시작해야함.